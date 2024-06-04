import json
from channels.generic.websocket import WebsocketConsumer

class ShoppingListConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'message': 'You are connected'
        }))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))

        self.channel_layer.group_send(
            'shopping_list',
            {
                'type': 'chat_message',
                'message': message
            }
        )

        def chat_message(self, event):
            message = event['message']

        # Send message to WebSocket
            self.send(text_data=json.dumps({
                'message': message
        }))

    async def update_message(self, event):
        await self.send(text_data=json.dumps(event))
