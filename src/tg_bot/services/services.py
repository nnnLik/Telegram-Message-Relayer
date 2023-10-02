from asgiref.sync import sync_to_async

from src.base.services.token import TokenServices
from src.tg_bot.bot import bot


@sync_to_async
def activate_user_token(token: str, chat_id: int, username: str) -> bool:
    token_generator: TokenServices = TokenServices()

    is_success: bool = token_generator.update_token_status(chat_id, username, token)

    return is_success


async def send_message_async(chat_id: int, message: str):
    await bot.send_message(chat_id, message)
