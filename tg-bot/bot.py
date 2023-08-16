from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from config.const import API_TOKEN


bot: Bot = Bot(API_TOKEN)
dp: Dispatcher = Dispatcher(bot)

dp.middleware.setup(LoggingMiddleware())
