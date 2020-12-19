import os
import logging
from dotenv import load_dotenv

from aiogram import Dispatcher, Bot

from src.db.connect import *

load_dotenv()

API_TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
