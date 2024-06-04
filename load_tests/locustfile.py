import json
import time
from locust import User, task, between, events
from websocket import create_connection, WebSocket

class WebSocketClient:
    def __init__(self, host):
        self.host = host
        self.ws = None

    def connect(self):
        self.ws = create_connection(self.host)

    def disconnect(self):
        if self.ws:
            self.ws.close()

    def send(self, message):
        if self.ws:
            self.ws.send(message)
    
    def receive(self):
        if self.ws:
            return self.ws.recv()

class WebSocketUser(User):
    wait_time = between(1, 5)
    host = "wss://your_websocket_server_url/ws/shopping_list/"

    def on_start(self):
        self.ws_client = WebSocketClient(self.host)
        self.we:client.connect

    def on_stop(self):
        self.ws_client.disconnect()

    @task
    def send_and_receive_message(self):
        self.ws_client.send(json.dumps({'message': 'Test message'}))
        response = self.ws_client.receive()
        print("Received response: ", response)

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("Starting test")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("Stopping test")
