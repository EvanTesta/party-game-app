from channels.generic.websocket import AsyncWebsocketConsumer
import json

CHAT_HISTORY = []


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("chat_group", self.channel_name)
        await self.accept()

        # Send last 50 messages to the new user
        for msg in CHAT_HISTORY[-50:]:
            await self.send(text_data=json.dumps(msg))

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')
        username = data.get('username', 'Anonymous')

        message_data = {
            'username': username,
            'message': message
        }

        # Save to chat history
        CHAT_HISTORY.append(message_data)

        # Broadcast message to everyone in the group
        await self.channel_layer.group_send(
            "chat_group",
            {
                "type": "chat.message",
                "message": message_data
            }
        )

    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event['message']))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("chat_group", self.channel_name)

class LeaderboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join the group so everyone can see updates
        await self.channel_layer.group_add("leaderboard", self.channel_name)
        await self.accept()
        await self.send_leaderboard()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("leaderboard", self.channel_name)

    async def send_leaderboard(self):
        users = await self.get_sorted_users()
        await self.send(text_data=json.dumps({
            "type": "leaderboard",
            "users": users
        }))

    async def leaderboard_update(self, event):
        await self.send_leaderboard()

    @staticmethod
    async def get_sorted_users():
        from .models import User
        # Query users and sort by score
        from asgiref.sync import sync_to_async
        users = await sync_to_async(list)(
            User.objects.order_by("-score").values("username", "score")[:10]
        )
        return users
