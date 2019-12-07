from django.core.management.base import BaseCommand, CommandError
import csv
import sys
from sightings.models import Sq
from __future__ import unicode_literals

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        field_names = [f.name for f in Sq._meta.fields]
        writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
        writer.writerow(field_names)
        for instance in Sq.objects.all():
            writer.writerow(getattr(instance, f) for f in field_names])

