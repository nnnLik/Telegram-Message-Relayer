import secrets
from typing import Dict

from django.contrib.auth.models import User

from .serializers import TelegramTokenSerializer
from .models import TelegramToken


class TokenGenerator:
    def generate(self, user: User) -> Dict[str, str]:
        self._delete_token_if_exists(user)
        token: str = self._generate_new_token()
        telegram_token: TelegramToken = self._create_telegram_token(user, token)
        serializer: TelegramTokenSerializer = TelegramTokenSerializer(telegram_token)
        result: Dict[str, str] = serializer.data

        return result

    def _delete_token_if_exists(self, user: User) -> None:
        TelegramToken.objects.filter(user=user).delete()

    def _generate_new_token(self) -> str:
        return secrets.token_hex(128)

    def _create_telegram_token(self, user: User, token: str):
        return TelegramToken.objects.create(user=user, token=token)
