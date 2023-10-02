from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from config.settings.const import TG_API_TOKEN

bot: Bot = Bot(TG_API_TOKEN)
dp: Dispatcher = Dispatcher(bot)

dp.middleware.setup(LoggingMiddleware())
