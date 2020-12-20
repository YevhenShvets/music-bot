from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


callback_form = CallbackData('post', 'id', 'action')


def create_inline_for_film(film_id):
    keyboard = InlineKeyboardMarkup()
    but_delete = InlineKeyboardButton("✖", callback_data=callback_form.new(id="-", action="delete"))
    but_info = InlineKeyboardButton("Треки", callback_data=callback_form.new(id=film_id, action="film-music"))
    keyboard.add(but_info, but_delete)
    return keyboard


def create_inline_for_film_list(films):
    keyboard = InlineKeyboardMarkup()
    button_next = InlineKeyboardButton(text="▶", callback_data=callback_form.new(id="-", action="next"))
    button_back = InlineKeyboardButton(text="◀", callback_data=callback_form.new(id="-", action="back"))
    button_delete = InlineKeyboardButton("✖", callback_data=callback_form.new(id="-", action="delete"))
    rows = []
    for i in range(0, len(films), 1):
        but = InlineKeyboardButton(text=(i + 1).__str__(), callback_data=callback_form.new(id=films[i]['id'],
                                                                                           action="film"))
        rows.append(but)
    keyboard.add(*rows[:5])
    keyboard.add(*rows[5:])
    keyboard.add(button_back, button_delete, button_next)
    return keyboard


def create_inline_for_music(music_id):
    keyboard = InlineKeyboardMarkup()
    but_delete = InlineKeyboardButton("✖", callback_data=callback_form.new(id="-", action="delete"))
    but_like = InlineKeyboardButton("🖤", callback_data=callback_form.new(id=music_id, action="music-like"))
    keyboard.add(but_like, but_delete)
    return keyboard


def create_inline_for_music_list(musics):
    keyboard = InlineKeyboardMarkup()
    button_next = InlineKeyboardButton(text="▶", callback_data=callback_form.new(id="-", action="next"))
    button_back = InlineKeyboardButton(text="◀", callback_data=callback_form.new(id="-", action="back"))
    button_delete = InlineKeyboardButton("✖", callback_data=callback_form.new(id="-", action="delete"))
    rows = []
    for i in range(0, len(musics), 1):
        but = InlineKeyboardButton(text=(i + 1).__str__(), callback_data=callback_form.new(id=musics[i]['id'],
                                                                                           action="music"))
        rows.append(but)
    keyboard.add(*rows[:5])
    keyboard.add(*rows[5:])
    keyboard.add(button_back, button_delete, button_next)
    return keyboard

