import os
import logging
from dotenv import load_dotenv

from aiogram import Dispatcher, Bot

load_dotenv()

API_TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
