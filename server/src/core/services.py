import secrets
from typing import Dict

from django.contrib.auth.models import User

from rest_framework import status

from .serializers import TelegramTokenSerializer
from .models import TelegramToken


class TokenServices:
    def generate(self, user: User) -> Dict[str, str]:
        self._delete_token_if_exists(user)
        token: str = self._generate_new_token()
        telegram_token: TelegramToken = self._create_telegram_token(user, token)
        serializer: TelegramTokenSerializer = TelegramTokenSerializer(telegram_token)
        result: Dict[str, str] = serializer.data

        return result

    def update_token_status(
        self,
        chat_id: int,
        username: str,
        token: str,
    ) -> None:
        try:
            telegram_token = TelegramToken.objects.get(token=token)
        except TelegramToken.DoesNotExist:
            return {
                "error": "Token not found for the given User."
            }, status.HTTP_400_BAD_REQUEST

        telegram_token.activate_token(chat_id=chat_id, telegram_username=username)

        return {"message": "Token updated successfully"}, status.HTTP_200_OK

    def _delete_token_if_exists(self, user: User) -> None:
        TelegramToken.objects.filter(user=user).delete()

    def _generate_new_token(self) -> str:
        return secrets.token_hex(128)

    def _create_telegram_token(self, user: User, token: str):
        return TelegramToken.objects.create(user=user, token=token)


class MessageServices:
    def create_msg(self, user: User, msg: str):
        ...
