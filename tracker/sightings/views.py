from django.http import HttpResponse
from django.shortcuts import render
from .models import Sq
from .forms import SqForm 
from django.shortcuts import redirect
from django.db.models import Count
from django.db.models import Avg, Max, Min

#This view shows the home page with links to add new squirrel sightings, update existing sightings, 
#and see statistics of specific attributes
def all_sq(request):
    sqs = Sq.objects.order_by('-Date')
    context = {
        'sqs': sqs,
    }
    return render(request, 'sightings/all.html', context)

#This view shows the update page
def edit_sq(request,Unique_Squirrel_ID):
    sq = Sq.objects.get(Unique_Squirrel_ID = Unique_Squirrel_ID)
    if request.method == 'POST':
        form = SqForm(request.POST, instance = sq)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SqForm(instance = sq)
    context = {
            'form': form,
    }
    return render(request,f'sightings/edit.html',context)

#This view shows the add page 
def add_sq(request):
    if request.method == 'POST':
        form = SqForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings')
    else:
        form =SqForm()
    context={
            'form': form,
    }
    return render(request, 'sightings/edit.html',context)

#This view shows statistics of different attributes
def stats(request):
    attributes = ['Age','Date','Primary_Fur_Color','Running','Chasing','Climbing','Eating','Foraging','Kuks','Quaas']
    values={i:{} for i in attributes}
    for item in values.keys():
        for each in Sq.objects.values(item).annotate(count=Count(item)):
            values[item][each[item]] = each['count']
    x = Sq.objects.aggregate(avg_=Avg('Longitude'), max_=Max('Longitude'),min_= Min('Longitude'))
    y = Sq.objects.aggregate(avg_=Avg('Latitude'), max_=Max('Latitude'),min_=Min('Latitude'))
    context ={
            'values':values,
            'x':x,
            'y':y,
    }
    return render(request,'sightings/stats.html',context)

#This view shows home page of all apps
def home(request):
    return render(request,'sightings/home.html')
