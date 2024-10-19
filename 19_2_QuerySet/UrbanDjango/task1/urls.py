from django.urls import path
from . import views

urlpatterns = [
    path('create_objects/', views.create_objects, name='create_objects'),
]