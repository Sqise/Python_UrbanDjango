from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Подключаем маршруты приложения blog
    path('', views.post_list, name='post_list'),
]