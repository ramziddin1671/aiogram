from aiogram import types
from data.config import ADMINS
from loader import dp
from filters.private_chat import IsPrivate


# Echo bot
@dp.message_handler(IsPrivate(), state=None)
async def bot_echo(message: types.Message):
    await message.answer("Ortiqcha habarlar qabul qilinmaydi!")
