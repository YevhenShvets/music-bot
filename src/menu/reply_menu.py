from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton


main_text = "Головна🌐"
my_music_text = "Мій плейлист🎶"

main_reply_menu = ReplyKeyboardMarkup(resize_keyboard=True)
but1 = KeyboardButton(main_text)
but2 = KeyboardButton(my_music_text)
main_reply_menu.add(but1)
main_reply_menu.add(but2)

