from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

# kim dur rasm yuborsa javob qaytaradi
@dp.message_handler(content_types='photo')
async def photo_handler(message: types.Message):
    await message.answer(f"bu qanday rasm")


@dp.message_handler(content_types='document')
async def photo_handler(message: types.Message):
    await message.answer(f"bu qanday dakument")


@dp.message_handler(content_types='sticker')
async def photo_handler(message: types.Message):
    await message.answer(f"qoil zor stiker ekan")


@dp.message_handler(content_types='voice')
async def photo_handler(message: types.Message):
    await message.answer(f"yaxshi eshitmadim")


@dp.message_handler(content_types='contact')
async def photo_handler(message: types.Message):
    await message.answer(f"kim bu odam")