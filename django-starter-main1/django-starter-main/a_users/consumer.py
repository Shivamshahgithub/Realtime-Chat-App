import json
from channels.generic.websocket import AsyncWebsocketConsumer

class GroupChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        self.group_room = f"group_{self.group_name}"

        # Join group room
        await self.channel_layer.group_add(
            self.group_room,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave group room
        await self.channel_layer.group_discard(
            self.group_room,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = self.scope['user'].username

        # Broadcast message to the group
        await self.channel_layer.group_send(
            self.group_room,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
