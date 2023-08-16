from aiogram.types import Message
from aiogram import Bot, Dispatcher
from src.tg_bot.services import activate_user_token

from src.tg_bot.config.message import msg
from src.tg_bot.handlers.utils import get_token


def setup(dp: Dispatcher, bot: Bot):
    @dp.message_handler(commands=["start"])
    async def start(message: Message):
        await message.answer(msg.start)

    @dp.message_handler(commands=["help"])
    async def help(message: Message):
        await message.answer(msg.help)

    @dp.message_handler(commands=["token"])
    async def activate_token(message: Message):
        token: str = await get_token(message.text)
        if token is None:
            await message.answer(msg.token_updating_failed)

        chat_id: int = message.chat.id
        username: str = message.from_user.username

        is_success: bool = await activate_user_token(token, chat_id, username)

        if is_success:
            await message.answer(msg.token_updated_successfully)
        else:
            await message.answer(msg.token_updating_failed)
