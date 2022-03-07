from channels.routing import ProtocolTypeRouter,URLRouter
import os
from channels.auth import AuthMiddlewareStack
import restfulapi.routing
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rest_test.settings")
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    # (your routes here)
    'http' : django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            restfulapi.routing.websocket_urlpatterns
        )
    )
})