from aiogram.types import Message
from aiogram import Bot, Dispatcher
from src.services import activate_user_token

from config.message import msg


def setup(dp: Dispatcher, bot: Bot):
    @dp.message_handler(commands=["start"])
    async def start(message: Message):
        print("dfewe")
        await message.answer(msg.start)

    @dp.message_handler(commands=["help"])
    async def help(message: Message):
        await message.answer(msg.help)

    @dp.message_handler(commands=["token"])
    async def activate_token(message: Message):
        try:
            _, token = message.text.split()
            chat_id: int = message.chat.id
            username: str = message.from_user.username
            is_success: bool = await activate_user_token(token, chat_id, username)
            if is_success:
                await message.answer(msg.token_updated_successfully)
        except ValueError:
            await message.answer(msg.token_updating_failed)
