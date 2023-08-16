from rest_framework import serializers

from .models import TelegramToken


class TelegramTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramToken
        fields = (
            "id",
            "token",
        )


class TokenUpdateSerializer(serializers.Serializer):
    chat_id = serializers.CharField(max_length=256)
    username = serializers.CharField(max_length=256)
    token = serializers.CharField(max_length=256)


class SendTelegramMessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=1024)
