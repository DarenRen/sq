from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_sq),
    path('<Unique_Squirrel_ID>/', views.edit_sq, name = 'edit'),
    ]
