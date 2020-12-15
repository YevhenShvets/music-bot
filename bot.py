import logging
from aiogram import executor
from src.core.Core import dp

from src.commands.help import *

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
