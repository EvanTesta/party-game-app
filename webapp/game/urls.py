from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('game/', views.game, name='game'),
    path('chat/', views.chat_room, name='chat'),
    path('submit_user/', views.submit_user, name="submit_user"),
    path('get_challenge/', views.get_challenge, name='get_challenge'),
    path('process_result/', views.process_result, name="process_result"),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
