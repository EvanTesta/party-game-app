"""
ASGI config for webapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

# CHAT GPT
import os
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import game.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,  # <-- route normal HTTP requests here
    "websocket": SessionMiddlewareStack(
        URLRouter(
            game.routing.websocket_urlpatterns
        )
    ),
})