from django.urls import path
from appadmin import consumers

websocket_urlpatterns = [
    # url(r'^ws/msg/(?P<room_name>[^/]+)/$', consumers.SyncConsumer),
    path("ws/test_async" , consumers.ChatConsumer.as_asgi()),
]