from django.shortcuts import render


def index(request):
    return render(request, 'third_task/index.html')


def music_list(request):
    songs = {
        'song1': 'John Lennon - Imagine',
        'song2': 'Queen - Bohemian Rhapsody',
        'song3': 'Led Zeppelin - Stairway to Heaven',
    }
    context = {'songs': songs}
    return render(request, 'third_task/music_list.html', context)


def cart(request):
    return render(request, 'third_task/cart.html')
