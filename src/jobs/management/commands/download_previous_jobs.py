import uuid

from django.core.management.base import BaseCommand

from jobs.models import Job
from core.utils import PersistentStorage


class Command(BaseCommand):
    """ Management script to sync all previous jobs stored on persistent storage
    """

    def handle(self, *args, **kwargs):
        storage = PersistentStorage()
        job_ids = storage.list_jobs()
        for job_id in job_ids:
            Job.objects.get_or_create(id=uuid.UUID(job_id),
                                      defaults={'status': Job.PREVIOUS})
