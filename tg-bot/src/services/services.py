import logging

from httpx import Response

from bot import bot
from config.message import msg

from .http_client import DjangoHttpClient

logger = logging.getLogger(__name__)


async def activate_user_token(token: str, chat_id: int, username: str) -> bool:
    http_client = DjangoHttpClient(base_url="http://server:8000", timeout=60)
    response: Response = await http_client.update_token_status(chat_id, username, token)

    return await handle_response(response, chat_id)


async def handle_response(response: Response, chat_id: int) -> bool:
    try:
        response.raise_for_status()
        logger.info("Token status updated successfully")
        return True
    except Exception as e:
        logger.error("Failed to update token status: %s", e)
        await send_error_message(chat_id)
        return False


async def send_error_message(chat_id: int) -> None:
    await bot.send_message(chat_id, msg.send_message_error)
