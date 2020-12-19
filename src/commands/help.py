from aiogram import types
from src.core import dp


@dp.message_handler(commands='help')
async def send_help(message: types.Message):
    await message.answer(f"Привіт✋ *{message.from_user.full_name}*\nЦе бот для пошуку музики з фільмів 📽➡🎵"
                         f"\n/start - Розпочати", parse_mode=types.ParseMode.MARKDOWN)
