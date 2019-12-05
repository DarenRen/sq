from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Sq
from .forms import SqForm
def all_sq(request):
    sqs = Sq.objects.all()
    context = {
        'Squirrels': sqs,
    }
    return render(request, 'sightings/all.html', context)

