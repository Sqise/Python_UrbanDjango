from django.urls import path
from task5 import views

urlpatterns = [
    path('', views.sign_up_by_html, name='sign_up_by_html'),
    path('django_sign_up', views.sign_up_by_django, name='sign_up_by_django'),
    path('success/<str:username>/', views.success, name='success'),
]