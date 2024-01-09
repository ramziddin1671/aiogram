from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, CommandSettings
from filters.private_chat import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/admin - Admin uchun habar")
    
    await message.answer("\n".join(text))


@dp.message_handler(CommandSettings())
async def bot_help(message: types.Message):
    text = ("Sozlamalar bo'limi")

    await message.answer(text)
