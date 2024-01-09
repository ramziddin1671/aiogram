from keyboards.inline.Zarur_Amaliyot import RaxbarGxp
from keyboards.inline.locationKamitet import backbackGxp, RAXBARGxp
from loader import dp, bot
from data.config import ADMINS
import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, contact, message


@dp.callback_query_handler(text_contains="bossDusmatov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharm-gxp.uz/uploads/leadership/25a32ca49d570f44615b329751123b33.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Dusmatov Aziz Fayzamatovich\n'Zarur amaliyotlar markazi direktori'</b>\nQabul kunlari: 🕰 Juma 16:00-18:00",reply_markup=RAXBARGxp)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="bossIbragimov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharm-gxp.uz/uploads/leadership/ce669a153be6c1a85403366194bf1a2b.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Ibragimov Avazbek Baxtiyarovich\n'Zarur amaliyotlar markazi direktor o‘rinbosari'</b>\nQabul kunlari: 🕰 Juma 16:00-18:00",reply_markup=RAXBARGxp)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="raxbarcancelGxp")
async def kamitet_boss(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Raxbarni tanlang</b> 📞 (+99871) 203-30-32", reply_markup=RaxbarGxp)
    await call.answer(cache_time=60)
