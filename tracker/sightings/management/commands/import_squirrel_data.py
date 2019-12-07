from django.core.management.base import BaseCommand
import csv
from sightings.models import Sq
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            if item['Age'] == '?':
                item['Age'] = ''
            s = Sq(
                Longitude = item['X'],
                Latitude = item['Y'],
                Unique_Squirrel_ID = item['Unique Squirrel ID'],
                Shift = item['Shift'],
                Date = item['Date'],
                Age = item['Age'],
                Primary_Fur_Color = item['Primary Fur Color'],
                Location = item['Location'],
                Specific_Location = item['Specific Location'],
                Running = (item['Running'] == 'true'),
                Chasing = (item['Chasing'] == 'true'),
                Climbing = (item['Climbing'] == 'true'),
                Eating = (item['Eating'] == 'true'),
                Foraging = (item['Foraging'] == 'true'),
                Other_Activities = item['Other Activities'],
                Kuks = (item['Kuks'] == 'true'),
                Quaas = (item['Quaas'] == 'true'),
                Moans = (item['Moans'] == 'true'),
                Tail_Flags = (item['Tail flags'] == 'true'),
                Tail_Twitches = (item['Tail twitches'] == 'true'),
                Approaches = (item['Approaches']== 'true'),
                Indifferent = (item['Indifferent']== 'true'),
                Runs_From = (item['Runs from']== 'true'),
            )
            s.save()
