from django.shortcuts import render
from channels.generic.websocket import AsyncWebsocketConsumer
import json


# Create your views here.
def game(request):
  return render(request, "game.html")

class LiveConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "live_updates"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', '')

        # Broadcast to all connected clients
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "send_message",
                "message": message
            }
        )

    async def send_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"]
        }))
