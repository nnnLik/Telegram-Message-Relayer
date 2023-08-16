from aiogram.utils import executor
import logging
import sys

from bot import dp, bot
from src.handlers import setup


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    setup(dp, bot)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
