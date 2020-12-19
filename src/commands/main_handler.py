from aiogram import types
from src.core import dp

from src.menu.reply_menu import main_text, my_music_text
from src.core.Core import bot


@dp.message_handler(content_types=['text'])
async def main_command(message: types.Message):
    if message.text == main_text:
        await bot.send_message(message.from_user.id, "/list - список фільмів", parse_mode="Markdown")
    elif message.text == my_music_text:
        await bot.send_message(message.from_user.id, "Music", parse_mode="Markdown")
    else:
        await bot.send_message(message.from_user.id, "Немає результатів", parse_mode="Markdown")


