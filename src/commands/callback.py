from aiogram import types
from src.core import dp
from pathlib import Path

from src.core.Core import bot
from src.db.select import get_film
from src.serializer.film_serializer import get_film_info
from src.menu.inline_menu import create_inline_for_film


@dp.callback_query_handler(lambda c: True)
async def callback_handler(callback_query: types.CallbackQuery):
    if callback_query.id:
        data = callback_query.data.split("_")
        if data[0] == "delete":
            await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

        elif data[0] == "film-music":
            await bot.send_message(callback_query.message.chat.id, "Message", parse_mode="Markdown")

        elif data[0] == "film":
            film = get_film(int(data[1]))
            film_serialize = get_film_info(film)

            base_dir = Path(__file__).resolve().parent.parent.parent
            base_dir = base_dir.joinpath('data/img/')
            await bot.send_photo(callback_query.message.chat.id,
                                 open(base_dir.joinpath(film['image_url']), 'rb'),
                                 film_serialize,
                                 reply_markup=create_inline_for_film(film['id']),
                                 parse_mode="Markdown")
