from django.shortcuts import render
from django.http import HttpResponse
from .models import Sq
from .forms import SqForm 
from django.shortcuts import redirect

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
    return render(request,f'sightings/{Unique_Squirrel_ID}',context)


# Create your views here.
