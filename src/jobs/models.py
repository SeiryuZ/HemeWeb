import os
import subprocess
import uuid

from django.conf import settings
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator
from django.db import models
from django.db import transaction

from django_rq import job


def job_directory_path(instance, filename):
    """ Function to generate the correct upload path folder
        Every job should have its own folder
        <upload_dir>/<hex-id-of-job>/<filename>
    """
    return os.path.join(settings.JOB_FILES_UPLOAD_DIR,
                        instance.id.hex,
                        'inputs',
                        filename)


@job
def run_job(job_instance):
        """ Function to be called in the background to run the submitted job
            This function will compose the correct command for the job
            and make sure that the stdout and stderr of the command is correctly
            piped into the correct files
        """

        command = "export ANSIBLE_HOST_KEY_CHECKING=False; \
        export AWS_SECRET_ACCESS_KEY={}; \
        export AWS_ACCESS_KEY_ID={}; \
        /var/www/hemeweb/virtualenv/bin/ansible-playbook \
        -u ubuntu \
        --extra-vars 'image={} master_ip={} worker_node_count={}  \
        instance_tags={} input={} output={} \
        worker_instance_type={} log_file={} core_count={}' \
        jobs/scripts/aws_ec2.yml\
        ".format(
            settings.AWS_SECRET_ACCESS_KEY,
            settings.AWS_ACCESS_KEY_ID,
            settings.HEMEWEB_IMAGE_ID,
            settings.HOST_IP,
            job_instance.instance_count,
            "job-{}".format(job_instance.id),
            job_instance.configuration_file.name,
            job_instance.get_result_directory_path(),
            job_instance.get_instance_id(),
            job_instance.get_log_file_path('hemelb'),
            job_instance.get_core_count()
        )

        with open(job_instance.get_log_file_path('stdout'), 'w') as stdout_file:
            with open(job_instance.get_log_file_path('stderr'), 'w') as stderr_file:
                # Update the status first
                with transaction.atomic():
                    job_instance.status = job_instance.RUNNING
                    job_instance.save(update_fields=['status'])

                # Run long running job
                completed = subprocess.call(command,
                                            stdout=stdout_file,
                                            stderr=stderr_file,
                                            shell=True)

                # Update the status of job accordingly
                if completed == 0:
                    job_instance.status = job_instance.DONE
                else:
                    job_instance.status = job_instance.FAILED
                job_instance.save(update_fields=['status'])


class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    configuration_file = models.FileField(upload_to=job_directory_path,
                                          verbose_name="Config (.xml)")
    input_file = models.FileField(upload_to=job_directory_path,
                                  verbose_name="Input (.gmy)")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    INSTANCE_CHOICES = (
        (2, '2 Cores'),
        (4, '4 Cores'),
        (8, '8 Cores'),
        (16, '16 Cores'),
    )
    instance_type = models.IntegerField(INSTANCE_CHOICES, default=2)
    instance_count = models.IntegerField(default=1, validators=[MaxValueValidator(36)])

    ADDED = 1
    QUEUED = 2
    RUNNING = 10
    DONE = 3
    FAILED = 0
    STATUS_CHOICES = (
        (ADDED, 'Added'),
        (QUEUED, 'Queued'),
        (RUNNING, 'Running'),
        (DONE, 'Done'),
        (FAILED, 'Failed'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=ADDED)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.id.hex

    def get_absolute_url(self):
        return reverse('jobs:details', kwargs={"pk": str(self.id)})

    def get_job_directory_path(self):
        return os.path.join(settings.JOB_FILES_UPLOAD_DIR,
                            self.id.hex)

    def get_log_directory_path(self):
        return os.path.join(self.get_job_directory_path(),
                            'logs')

    def get_result_directory_path(self):
        return os.path.join(self.get_job_directory_path(),
                            'result')

    def get_log_file_path(self, log_type):
        return os.path.join(self.get_log_directory_path(),
                            log_type)

    def get_instance_id(self):
        if self.instance_type == 2:
            return 'c4.large'
        elif self.instance_type == 4:
            return 'c4.xlarge'
        elif self.instance_type == 8:
            return 'c4.2xlarge'
        elif self.instance_type == 16:
            return 'c4.4xlarge'

    def get_core_count(self):
        return self.instance_count * self.instance_type

    def get_output(self, log_type):
        key = "{}:log:{}".format(self.id.hex, log_type)

        # Hit the cache first
        output = cache.get(key)

        # Cache Miss
        if output is None:

            # Read from the file, this is slow
            with open(self.get_log_file_path(log_type), 'r') as _file:
                output = _file.read()

            # Save it to the cache, depending on the likelihood of the content
            # being updated
            if self.status != self.DONE and self.status != self.FAILED:
                cache.set(key, output, timeout=5)
            else:
                cache.set(key, output, timeout=5000)

        return output

    def prepare_directories(self):
        os.makedirs(self.get_log_directory_path())
        open(self.get_log_file_path('stdout'), 'a').close()
        open(self.get_log_file_path('stderr'), 'a').close()

    def enqueue_job(self, async=True):
        """ Function to queue job execution to background worker.
        """
        if async:
            run_job.delay(self)
        else:
            run_job(self)
