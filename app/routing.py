from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/sc/<groupname>/', consumers.MySyncConsumer.as_asgi()),
    path('ws/asc/<groupname>/', consumers.MyAsyncConsumer.as_asgi())

]


