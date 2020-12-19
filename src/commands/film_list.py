from aiogram import types
from src.core import dp
from src.db.select import get_film, get_films_name
from src.serializer.film_serializer import get_name_films_serealizer


@dp.message_handler(commands='list')
async def get_films(message: types.Message):
    films = await get_films_name()
    films_serealize = get_name_films_serealizer(films)

    keyboard = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton(text="--->", callback_data="next")
    button_back = types.InlineKeyboardButton(text="<---", callback_data="back")

    rows = []
    for i in range(0, len(films), 1):
        but = types.InlineKeyboardButton(text=(i+1).__str__(), callback_data=f"film_{films[i]['id']}")
        rows.append(but)
    keyboard.add(*rows[:5])
    keyboard.add(*rows[5:])
    keyboard.add(button_back, button_next)
    await message.answer(films_serealize, reply_markup=keyboard, parse_mode=types.ParseMode.MARKDOWN)
