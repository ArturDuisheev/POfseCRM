from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from chat.models import Message
from chat.serializers import MessageSerializer


class SendMessageAPIView(APIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = [IsAuthenticated]

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        channel_layer = get_channel_layer()
        room_name = self.kwargs['room_name']
        message = request.data.get('message')
        async_to_sync(channel_layer.group_send)(
            room_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
        return Response({'status': 'Ваше сообщение успешно отправлено!'})