import uuid
import os

from django.conf import settings
from django.db import models


def job_directory_path(instance, filename):
    """ Function to generate the correct upload path folder
        Every job should have its own folder
        <upload_dir>/<hex-id-of-job>/<filename>
    """
    return os.path.join(settings.JOB_FILES_UPLOAD_DIR,
                        instance.id.hex,
                        'inputs',
                        filename)


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
