from django.http import HttpResponse
from django.shortcuts import render
from .models import Sq
from .forms import SqForm 
from django.shortcuts import redirect

def all_sq(request):
    sqs = Sq.objects.all()
    context = {
        'Squirrels': sqs,
    }
    return render(request, 'sightings/all.html', context)

def edit_sq(request,Unique_Squirrel_ID):
    sq = Sq.objects.get(id= Unique_Squirrel_ID)
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


def add_sq(request):
    if request.method == 'POST':
        form = SqForm(request.POST)
        if form.is_valis():
            form.save()
            return redirect('/sightings')
    else:
        form =SqForm()
    context={
            'form': form,
            }
    return render(request, 'sightings/edit.html',context)
