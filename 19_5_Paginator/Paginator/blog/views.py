# blog/views.py
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Сортировка по дате

    # Получаем из GET-запроса количество элементов на странице, по умолчанию - 5
    items_per_page = request.GET.get('items_per_page', 5)
    try:
        items_per_page = int(items_per_page)
    except ValueError:
        items_per_page = 5  # Устанавливаем значение по умолчанию, если передано некорректное значение

    paginator = Paginator(posts, items_per_page)  # Пагинатор с указанным количеством элементов на странице

    page_number = request.GET.get('page')  # Получаем номер текущей страницы из URL
    page_obj = paginator.get_page(page_number)  # Получаем объекты для текущей страницы

    return render(request, 'blog/post_list.html', {
        'page_obj': page_obj,
        'items_per_page': items_per_page,  # Передаем в шаблон текущий выбор количества элементов
    })