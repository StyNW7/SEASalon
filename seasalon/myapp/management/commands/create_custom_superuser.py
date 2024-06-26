# myapp/management/commands/create_custom_superuser.py

from django.core.management.base import BaseCommand
from myapp.models import CustomRole  # Ganti 'myapp' dengan nama aplikasi Anda

class Command(BaseCommand):
    help = 'Create a superuser with additional fields'

    def handle(self, *args, **kwargs):
        username = input('Enter username: ')
        email = input('Enter email address: ')
        full_name = input('Enter full name: ')
        phone_number = input('Enter phone number: ')
        password = input('Enter password: ')

        user = CustomRole.objects.create_superuser(username=username, email=email, password=password)
        user.full_name = full_name
        user.phone_number = phone_number
        user.role = 'admin'  # Setel role sebagai admin
        user.save()

        self.stdout.write(self.style.SUCCESS('Superuser created successfully!'))
