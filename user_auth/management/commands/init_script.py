from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Creates client and staff user'

    def add_arguments(self, parser):
        pass
        # parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        if not User.objects.filter(username="client").count():
            client = User.objects.create_user('client', 'client@gmail.com', 'client')
        if not User.objects.filter(username="staff").count():
            staff = User.objects.create_user('staff', 'staff@gmail.com', 'staff')
            staff.is_staff = True
            staff.is_superuser = True
            staff.save()
        self.stdout.write(self.style.SUCCESS('Successfully created users Client and Staff'))
        self.stdout.write('Staff -> username: staff, password: staff')
        self.stdout.write('Client -> username: client, password: client')
        
