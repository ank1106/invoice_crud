from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Creates client and staff user'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # create client
        user, created = User.objects.get_or_create(username="client")
        user.email = "client@gmail.com"
        user.is_staff = True # for demo purpose
        user.set_password('client')
        user.save()
        
        # create staff
        user, created = User.objects.get_or_create(username="staff")
        user.email = "staff@gmail.com"
        user.is_staff = True
        user.is_superuser = True
        user.set_password('staff')
        user.save()
        self.stdout.write('Staff -> username: staff, password: staff')
        self.stdout.write('Client -> username: client, password: client')
        self.stdout.write(self.style.SUCCESS('Successfully created users Client and Staff'))
        
