import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']
        except (json.JSONDecodeError, KeyError) as e:
            # Обработка ошибки разбора JSON-строки или отсутствия поля `message`
            error_message = f"Error: {str(e)}"
            await self.send(text_data=json.dumps({
                'error': error_message
            }))
        else:
            await self.send(text_data=json.dumps({
                'message': message
            }))

    async def chat_message(self, event):
        message = event['message']

        # Отправить сообщение в WebSocket соединении
        await self.send(text_data=json.dumps({
            'message': message
        }))