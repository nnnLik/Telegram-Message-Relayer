import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode

API_TOKEN = "6360409566:AAE0l-dCI3OEtLz0nuJROz-iV8DvYZuC1Qg"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    text = md.text(md.text('Привет, {0.first_name}!\nЯ телеграм-бот, который повторяет ваше сообщение.'.format(message.from_user), md.bold('Жду вашего сообщения...')))
    await message.reply(text, parse_mode=ParseMode.MARKDOWN)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Вы сказали: " + message.text)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
