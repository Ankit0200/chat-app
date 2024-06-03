"""
ASGI config for chat_application project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""


import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
import app.routing as routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_application.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(routing.websocket_urlpatterns)
})
#
"""
ASGI config for chat_application project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# import handling_chat.routing as routing
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_application.settings')
#
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#          routing.websocket_urlpatterns
#         )
#     ),
# })
