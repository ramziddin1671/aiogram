from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def get_file_id_p(message: types.Message):
    await message.reply(message.document.file_id)