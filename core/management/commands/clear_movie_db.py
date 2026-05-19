from django.core.management.base import BaseCommand
from core.models import Movie

class Command(BaseCommand):
    def handle(self, *args, **options):
        Movie.objects.all().delete()