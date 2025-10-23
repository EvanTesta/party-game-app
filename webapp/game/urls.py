from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('game/', views.game, name='game'),
    path('chat/', views.chat_room, name='chat'),
    #path('leaderboard/', views.leaderboard, name='leaderboard'),
]
