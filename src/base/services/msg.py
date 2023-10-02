import asyncio
import logging

from django.contrib.auth.models import User

from src.core.models import MessageHistory, TelegramToken
from src.tg_bot.services.services import send_message_async

logger = logging.getLogger(__name__)


class MessageServices:
    def send_message(self, user: User, msg: str) -> bool:
        is_sended: bool | None = None
        telegram_token: TelegramToken = self._get_data(user)

        chat_id: int = telegram_token.chat_id
        username: str = telegram_token.tg_username

        final_msg: str = self._create_msg(username, msg)

        try:
            self.__run_send_message_async(chat_id=chat_id, message=final_msg)
        except Exception as e:
            logger.critical(f"Error sending message: {e}")
            is_sended: bool = False
        is_sended: bool = True

        if is_sended:
            self._save_msg_to_history(user, chat_id, msg)

    def _get_data(self, user: User) -> TelegramToken:
        return TelegramToken.objects.get(user=user)

    def _create_msg(self, username: str, msg: str) -> str:
        return f"{username}, я получил от тебя сообщение:\n\n{msg}"

    def __run_send_message_async(self, chat_id: int, message: str):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(
            send_message_async(
                chat_id=chat_id,
                message=message,
            )
        )
        loop.close()

    def _save_msg_to_history(self, user: User, chat_id: int, msg: str) -> None:
        MessageHistory.objects.create(
            user=user,
            content=msg,
            chat_id=chat_id,
        )
