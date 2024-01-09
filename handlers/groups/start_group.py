import logging

from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp
from keyboards.default.menuKeyboard import menu
from filters.group_chat import IsGroup



# deep_link bu qaysi saytdan kelgan foydalanuvchilarni nazorat qilish imkoni
@dp.message_handler(IsGroup(), CommandStart())
async def bot_start(message: types.Message):
    text = f'Salom, {message.from_user.full_name}!\n'
    text += f"<b>Siz FARMATSEVTIKA TARMOGʻINI RIVOJLANTIRISH AGENTLIGI </b>\n"
    text += f"bo'tidan guruxlarda foydalana olmaysiz iltimos bo'tni o'ziga o'ting!"
    await message.answer(text)