from aiogram import types
from src.core import dp
from src.db.select import select_films_name
from src.serializer.film_serializer import get_name_films_serealizer
from src.menu.inline_menu import create_inline_for_film_list


@dp.message_handler(commands='list')
async def get_films(message: types.Message):
    films = await select_films_name()
    films_serealize = get_name_films_serealizer(films)

    keyboard = create_inline_for_film_list(films)
    await message.answer(films_serealize, reply_markup=keyboard, parse_mode=types.ParseMode.MARKDOWN)
