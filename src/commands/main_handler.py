from aiogram import types
from src.core import dp

from src.menu.reply_menu import main_text, my_music_text
from src.core.Core import bot
from src.commands.my import my_playlist

from src.db.select import select_search_films_name
from src.serializer.film_serializer import get_name_films_serealizer
from src.menu.inline_menu import create_inline_for_film_list


@dp.message_handler(content_types=['text'])
async def main_command(message: types.Message):
    if message.text == main_text:
        await message.answer("/list - список фільмів", parse_mode="Markdown")
    elif message.text == my_music_text:
        await my_playlist(message)
    else:
        search_text = message.text
        films = await select_search_films_name(search_text)
        if films:
            films_serealize = get_name_films_serealizer(films)

            keyboard = create_inline_for_film_list(films)
            await message.answer(films_serealize, reply_markup=keyboard, parse_mode="Markdown")
        else:
            await message.answer("Немає результатів", parse_mode="Markdown")


