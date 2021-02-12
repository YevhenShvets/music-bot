from aiogram import types
from src.core import dp


from src.core.Core import bot
from src.db.select import select_liked_music
from src.serializer.music_serializer import get_music_list_serealizer
from src.menu.inline_menu import create_inline_for_music_list


@dp.message_handler(commands='my')
async def my_playlist(message: types.Message):
    user_id = message.from_user.id
    music = select_liked_music(user_id)
    music_serialize = get_music_list_serealizer(music)
    if music_serialize != "":
        await bot.send_message(message.chat.id,
                           music_serialize,
                           reply_markup=create_inline_for_music_list(music),
                           parse_mode="Markdown")
    else:
        await bot.send_message(message.chat.id,
                               "Музики немає",
                               parse_mode="Markdown")
