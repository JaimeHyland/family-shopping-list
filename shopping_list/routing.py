from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/shopping_list/', consumers.ShoppingListConsumer.as_asgi()),
]