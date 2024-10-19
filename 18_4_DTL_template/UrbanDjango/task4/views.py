from django.shortcuts import render


def index(request):
    return render(request, 'fourth_task/index.html')


def music_list(request):
    games = ['Atomic Heart', 'Cyberpunk 2077']
    context = {'games': games}
    return render(request, 'fourth_task/music_list.html', context)


def cart(request):
    return render(request, 'fourth_task/cart.html')
