from aiogram import types
from src.core import dp
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


@dp.message_handler(commands='help')
async def send_help(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
