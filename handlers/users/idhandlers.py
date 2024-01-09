from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp


SUPERUSER = [35824787]
BLACKLIST = []

@dp.message_handler(chat_id=SUPERUSER, text='secret')
async def id_fillter_example(message: types.Message):
    await message.answer(f"Xush kelibsiz admin")
