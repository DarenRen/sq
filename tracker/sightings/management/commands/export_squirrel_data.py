from django.core.management.base import BaseCommand, CommandError
import csv
import sys
from sightings.models import Sq

class Command(BaseCommand):
    def handle(self, *args, **options):
        field_names = [f.name for f in Sq._meta.fields]
        writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
        writer.writerow(field_names)
        for instance in model.objects.all():
            writer.writerow([unicode(getattr(instance, f)).encode('utf-8') for f in field_names])

