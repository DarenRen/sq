from django.shortcuts import render
from sightings.models import Sq
def map(request):
    sqs = Sq.objects.all()
    context = {
            'sqs': sqs,
    }
    return render(request, 'map/map.html', context)

