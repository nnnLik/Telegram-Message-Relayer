from rest_framework import serializers

from .models import TelegramToken


class TelegramTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramToken
        fields = (
            "id",
            "token",
        )


class SendTelegramMessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=1024)
