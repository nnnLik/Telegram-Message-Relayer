from rest_framework import serializers

from .models import MessageHistory, TelegramToken


class TelegramTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramToken
        fields = (
            "id",
            "token",
        )


class SendTelegramMessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=1024)


class MessageHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageHistory
        fields = (
            "id",
            "user",
            "content",
            "chat_id",
            "sended_at",
        )
