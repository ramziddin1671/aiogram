import logging

from keyboards.inline.AgentKeyboard import back_button, categoryAgent
from keyboards.inline.locationAgent import backagent
from keyboards.inline.referentagentkeyboard import Referent
from loader import dp, bot
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text="02_avgust")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos, kuting, yuborilmoqda!")
    url_document = "BQACAgIAAxkBAAIc02O3_8wyQ7EDgQ5V3hdSF4_mYLsvAAIHIQACXPDBSY7LF-_skz_6LQQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_document, caption="<b>Mahalliy va xorijiy dori vositalariga nisbatan belgilangan cheklangan narxlar toʼgʼrisidagi maʼlumotlar</b>",reply_markup=backagent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancelAgent")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.delete()
    await call.message.answer("Bo'limlardan birini tanlang: ", reply_markup=categoryAgent)
