from aiogram import types
from src.core import dp
from src.db.select import select_top_films_name, select_top_music
from src.serializer.film_serializer import get_name_films_serealizer
from src.serializer.music_serializer import get_music_list_serealizer
from src.menu.inline_menu import create_inline_for_film_list, create_inline_for_music_list


@dp.message_handler(commands='topmusic')
async def send_topmusic(message: types.Message):
    musics = select_top_music()
    music_serealize = get_music_list_serealizer(musics)

    keyboard = create_inline_for_music_list(musics)
    await message.answer(music_serealize, reply_markup=keyboard, parse_mode="Markdown")


@dp.message_handler(commands='topfilm')
async def send_topfilm(message: types.Message):
    films = await select_top_films_name()
    films_serealize = get_name_films_serealizer(films)

    keyboard = create_inline_for_film_list(films)
    await message.answer(films_serealize, reply_markup=keyboard, parse_mode="Markdown")

