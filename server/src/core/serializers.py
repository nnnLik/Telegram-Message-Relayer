from rest_framework.serializers import ModelSerializer

from .models import TelegramToken


class TelegramTokenSerializer(ModelSerializer):
    class Meta:
        model = TelegramToken
        fields = (
            "id",
            "token",
        )
