from django.urls import path
from . import views
from .models import Sq

urlpatterns = [
    path('', views.all_sq),
    path('add/', views.add_sq, name = 'add'),
    path('stats/',views.stats, name = 'stats'),
    path('<Unique_Squirrel_ID>/', views.edit_sq, name = 'edit'),
]
