from django.core.management.base import BaseCommand, CommandError
import csv
from sightings.models import Sq

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_name')

    def handle(self, *args, **options):
        file_name = options['file_name']
        field_names = [f.name for f in Sq._meta.fields]
        with open(file_name, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(field_names)
            for instance in Sq.objects.all():
                writer.writerow(getattr(instance, f) for f in field_names)

