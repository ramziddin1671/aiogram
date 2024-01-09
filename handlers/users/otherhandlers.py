from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

#is reply
@dp.message_handler(is_reply=True, commands='user_id')
async def reply_filter(message: types.Message):
    await message.answer(message.reply_to_message.from_user.id)

#send contact
@dp.message_handler(content_types='contact', is_sender_contact=True)
async def reply_filter(message: types.Message):
    await message.answer('Raxmat kantaktingiz qabul qilindi')


#send forward
@dp.message_handler(is_forwarded=True)
async def reply_filter(message: types.Message):
    await message.answer('Birovning xabari kerak emas')


#send forward
@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), commands='shaxsiy')
async def reply_filter(message: types.Message):
    await message.answer('Bu shaxsiy chat')