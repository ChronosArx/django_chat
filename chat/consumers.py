from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        self.user_id = self.channel_name
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user_name = text_data_json["username"]
        message = text_data_json["message"]

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "username": user_name,
                "message": message,
                "user_id": self.user_id,
            },
        )

    async def chat_message(self, event):
        user_name = event["username"]
        message = event["message"]
        user_id = event["user_id"]

        if self.user_id != user_id:
            await self.send(
                text_data=json.dumps({"username": user_name, "message": message})
            )
