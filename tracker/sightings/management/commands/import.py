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
            s = Sq(
                X = item['X'],
                Y = item['Y'],
                Unique_Squirrel_ID = item['Unique Squirrel ID'],
                Shift = item['Shift'],
                Date = item['Date'],
                Age = item['Date'],
                Primary_Fur_Color = item['Primary Fur Color'],
                Location = item['Location'],
                Specific_Location = item['Specific Location'],
                Running = (item['Running'] == 'True'),
                Chasing = (item['Chasing'] == 'True'),
                Climbing = (item['Climbing'] == 'True'),
                Eating = (item['Eating'] == 'True'),
                Foraging = (item['Foraging'] == 'True'),
                Other_Activities = item['Other Activities'],
                Kuks = (item['Kuks'] == 'True'),
                Quaas = (item['Quaas'] == 'True'),
                Moans = (item['Moans'] == 'True'),
                Tail_Flags = (item['Tail flags'] == 'True'),
                Tail_Twitches = (item['Tail twitches'] == 'True'),
                Approaches = (item['Approaches']== 'True'),
                Indifferent = (item['Indifferent']== 'True'),
                Runs_From = (item['Runs from']== 'True'),
            )
            s.save()
