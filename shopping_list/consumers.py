import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ShoppingListConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass

    async def update_message(self, event):
        await self.send(text_data=json.dumps(event))
