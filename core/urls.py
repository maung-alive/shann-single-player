from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('play', views.play, name='play'),
    path('play/game', views.game, name='game'),
    path('play/game/take', views.take, name='game-take')
]
