import os
import subprocess
import uuid

from django.conf import settings
from django.db import models

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
        command = [
            'cat',
            job_instance.configuration_file.name,
        ]

        with open(job_instance.get_log_file_path('stdout'), 'w') as stdout_file:
            with open(job_instance.get_log_file_path('stderr'), 'w') as stderr_file:
                subprocess.call(command, stdout=stdout_file, stderr=stderr_file)


class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    configuration_file = models.FileField(upload_to=job_directory_path)
    input_file = models.FileField(upload_to=job_directory_path)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    ADDED = 1
    QUEUED = 2
    DONE = 3
    FAILED = 0
    STATUS_CHOICES = (
        (ADDED, 'Added'),
        (QUEUED, 'Queued'),
        (DONE, 'Done'),
        (FAILED, 'Failed'),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=ADDED)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.id.hex

    def get_job_directory_path(self):
        return os.path.join(settings.JOB_FILES_UPLOAD_DIR,
                            self.id.hex)

    def get_log_directory_path(self):
        return os.path.join(self.get_job_directory_path(),
                            'logs')

    def get_log_file_path(self, log_type):
        return os.path.join(self.get_log_directory_path(),
                            log_type)

    def prepare_directories(self):
        os.makedirs(self.get_log_directory_path())

    def enqueue_job(self, async=True):
        """ Function to queue job execution to background worker.
        """
        if async:
            run_job.delay(self)
        else:
            run_job(self)


