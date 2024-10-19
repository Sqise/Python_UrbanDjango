from django.shortcuts import render

from .models import Buyer, Game


def create_objects(request):
    # СозданиеBUYER
    first_buyer = Buyer.objects.create(name='Vasya', balance=100.0, age=20)
    second_buyer = Buyer.objects.create(name='Petya', balance=200.0, age=25)
    third_buyer = Buyer.objects.create(name='Vitek', balance=300.0, age=17)

    # Создание GAMES
    game1 = Game.objects.create(title='Shashki', cost=10.0, size=1.0, description='Play Shashki', age_limited=False)
    game2 = Game.objects.create(title='Sudoku', cost=20.0, size=2.0, description='Play Sudoku', age_limited=True)
    game3 = Game.objects.create(title='Cards', cost=30.0, size=3.0, description='Play Cards', age_limited=True)

    # СвязываниеBUYER с GAMES
    game1.buyer.set((first_buyer, second_buyer, third_buyer))
    game2.buyer.set((first_buyer,))
    game3.buyer.set((second_buyer,))

    return render(request, 'task1/success.html')


# Создайте URL для вызова этой функции
from django.urls import path

urlpatterns = [
    path('create_objects/', create_objects, name='create_objects'),
]
