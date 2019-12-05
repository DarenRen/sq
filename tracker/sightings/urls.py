from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_sq)
    path('add/', views.sq_add),
    path('stats/', views.sq_stats),
    path('<int:sq_id>/', views.sq_details),
    ]
