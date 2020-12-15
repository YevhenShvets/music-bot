from aiogram import types
from src.core import dp
from pathlib import Path
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


@dp.message_handler(commands='help')
async def send_help(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    BASE_DIR = BASE_DIR.joinpath('data/img/')

    # await message.answer("Hello " + message.from_user.full_name +"   "+ BASE_DIR.joinpath(
    # 'data/img/img1.png').__str__())
    reply_keyboard =ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = KeyboardButton("Hello!!!!")
    but2 = KeyboardButton("Hi!")
    reply_keyboard.add(but1)
    reply_keyboard.add(but2)
    await message.answer_photo(open(BASE_DIR.joinpath('img1.png').__str__(), 'rb'), reply_markup=reply_keyboard)
