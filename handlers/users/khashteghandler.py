from aiogram import types
from aiogram.dispatcher import filters
from loader import dp


@dp.message_handler(hashtags=['money', 'sum', 'pul'])
@dp.message_handler(cashtags=['eur', 'sum', 'usd'])
async def photo_handler(message: types.Message):
    await message.answer(f"akang kuchaydi akang")
