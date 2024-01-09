from keyboards.inline.Ximiya_ketboard import categoryXimiya
from loader import dp, bot
import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, contact


@dp.message_handler(text="O'zKFITI")
async def kamitet(message: Message):
    await message.answer(f"<b>Hozirda dasturlash ishlari olib borilmoqda </b>")#, reply_markup=categoryXimiya)


@dp.message_handler(text="Sharq tabobati ITI")
async def kamitet(message: Message):
    await message.answer(f"<b>Hozirda dasturlash ishlari olib borilmoqda </b>")#, reply_markup=categoryXimiya)