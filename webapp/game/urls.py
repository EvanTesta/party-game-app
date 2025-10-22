from django.urls import path, re_path
from game import views

urlpatterns = [
  path('game/', views.game, name='game'),
]

websocket_urlpatterns = [
  re_path(r"ws/live/$", views.LiveConsumer.as_asgi(), name="live"),
]