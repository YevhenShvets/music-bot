from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_inline_for_film(film_id):
    keyboard = InlineKeyboardMarkup()
    but_delete = InlineKeyboardButton("✖", callback_data=f"delete_")
    but_info = InlineKeyboardButton("Треки", callback_data=f"film-music_{film_id}")
    keyboard.add(but_info, but_delete)
    return keyboard
