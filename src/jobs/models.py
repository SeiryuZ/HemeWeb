import os
import subprocess
import uuid

from django.conf import settings
from django.core.cache import cache
from django.core.urlresolvers import reverse
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
        # TODO: replace this with the correct hemelb command
        # command = [
            # 'cat',
            # job_instance.configuration_file.name,
        # ]

        command = "{} {} {} {} {} {} {} {} {}".format(
            'mpirun.openmpi',
            '--mca btl_tcp_if_include eth0',
            '-np 8',
            '--host hemelb-node-1,hemelb-node-2',
            'hemelb',
            '-in',
            job_instance.configuration_file.name,
            '-out',
            job_instance.get_result_directory_path(),
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

    configuration_file = models.FileField(upload_to=job_directory_path)
    input_file = models.FileField(upload_to=job_directory_path)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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
