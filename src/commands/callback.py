from aiogram import types
from src.core import dp
from pathlib import Path
import typing

from src.core.Core import bot
from src.db.select import select_film, select_music_list, select_music
from src.db.insert import insert_liked_music
from src.serializer.film_serializer import get_film_info_serealizer
from src.serializer.music_serializer import get_music_list_serealizer
from src.menu.inline_menu import create_inline_for_film,\
    callback_form, create_inline_for_music_list,\
    create_inline_for_music
from src.db.update import update_film_activity, update_music_activity


@dp.callback_query_handler(callback_form.filter(action='delete'))
async def callback_handler_delete(callback_query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)


@dp.callback_query_handler(callback_form.filter(action='film-music'))
async def callback_handler_film_music(callback_query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    film_id = callback_data['id']
    musics = select_music_list(film_id)
    music_serealize = get_music_list_serealizer(musics)
    await bot.send_message(callback_query.message.chat.id,
                           music_serealize,
                           reply_markup=create_inline_for_music_list(musics),
                           parse_mode="Markdown")


@dp.callback_query_handler(callback_form.filter(action='film'))
async def callback_handler_film_list(callback_query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    film_id = callback_data['id']
    film = select_film(int(film_id))
    film_serialize = get_film_info_serealizer(film)
    update_film_activity(int(film_id))
    base_dir = Path(__file__).resolve().parent.parent.parent
    base_dir = base_dir.joinpath('data/img/')
    await bot.send_photo(callback_query.message.chat.id,
                         open(base_dir.joinpath(film['image_url']), 'rb'),
                         film_serialize,
                         reply_markup=create_inline_for_film(film['id']),
                         parse_mode="Markdown")


@dp.callback_query_handler(callback_form.filter(action='music'))
async def callback_handler_music_list(callback_query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    music_id = callback_data['id']
    music = select_music(int(music_id))
    update_music_activity(int(music_id))

    base_dir = Path(__file__).resolve().parent.parent.parent
    base_dir = base_dir.joinpath('data/song/')
    await bot.send_audio(callback_query.message.chat.id,
                         open(base_dir.joinpath(music['url']), 'rb'),
                         title=music['name'],
                         performer=music['author'],
                         reply_markup=create_inline_for_music(music['id']),
                         parse_mode="Markdown")


@dp.callback_query_handler(callback_form.filter(action='music-like'))
async def callback_handler_music_like(callback_query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    music_id = callback_data['id']
    isAdd = insert_liked_music(callback_query.from_user.id, music_id)
    await callback_query.answer("Добавлено в плейлист✅" if isAdd else "Вилучено з плейлисту🚫")
