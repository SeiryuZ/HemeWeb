from django.core.management.base import BaseCommand

from core.utils import PersistentStorage


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        PersistentStorage().prepare_storage()
