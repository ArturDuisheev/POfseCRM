from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    message = serializers.CharField(max_length=1000)
    created_at = serializers.DateTimeField(format="%Y-%m-%d".replace(" ", "T"))
    updated_at = serializers.DateTimeField(format="%Y-%m-%d".replace(" ", "T"))

    class Meta:
        model = Message
        fields = '__all__'

        read_only_fields = ('created_at', 'updated_at')