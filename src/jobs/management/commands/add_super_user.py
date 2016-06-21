# This is a hack to create superuser from command line,
# because there is no nice way to create superuser with password with cmd line
# This is taken from http://stackoverflow.com/questions/23501933/cli-create-super-user-in-django-with-raw-python-no-python-shell
from optparse import make_option

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--user',
                    action='store',
                    default=None,
                    help='Username for new user'),
        make_option('--password',
                    action='store',
                    default=None,
                    help='User Password'),
        make_option('--email',
                    action='store',
                    default=None,
                    help='User Email Address'),
    )

    def handle(self, *args, **kwargs):
        user = User.objects.create_user(
            username=kwargs.get('user'),
            password=kwargs.get('password'),
            email=kwargs.get('email'),
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.save()
