# freya_backend_testing/management/commands/create_test_data.py
from django.core.management.base import BaseCommand
from freya_backend_testing.database_utils import create_test_data

class Command(BaseCommand):
    help = 'Create test data in PostgreSQL database.'

    def handle(self, *args, **kwargs):
        create_test_data()
        self.stdout.write(self.style.SUCCESS('Test data created successfully.'))