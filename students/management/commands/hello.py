from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Привет'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Привет'))