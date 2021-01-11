from aiogram import types
from src.core import dp


@dp.message_handler(commands='settings')
async def send_settings(message: types.Message):
    await message.answer("Settings", parse_mode="Markdown")
