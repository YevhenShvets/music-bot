from aiogram import types
from src.core import dp
from pathlib import Path

from src.db.insert import insert_user
from src.menu.reply_menu import main_reply_menu


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    BASE_DIR = BASE_DIR.joinpath('data/img/')

    # add user to database
    insert_user(message.from_user.id, message.from_user.full_name)

    # await message.answer("Hello " + message.from_user.full_name +"   "+ BASE_DIR.joinpath(
    # 'data/img/img1.png').__str__())

    await message.answer("/list - список фільмів\n/my - мій плейлист\n/topmusic - список популярних саунтреків\n/topfilm - список популярниз фільмів", parse_mode="Markdown")
