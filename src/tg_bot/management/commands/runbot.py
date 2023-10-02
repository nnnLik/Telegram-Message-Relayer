import logging
import sys

from django.core.management.base import BaseCommand

from aiogram.utils import executor

from src.tg_bot.bot import dp, bot
from src.tg_bot.handlers import setup


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    setup(dp, bot)


class Command(BaseCommand):
    help = "Run the Aiogram bot"

    def handle(self, *args, **options):
        self._runbot()

    def _runbot(self):
        executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
