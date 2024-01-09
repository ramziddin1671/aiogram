import logging

from keyboards.inline.AgentKeyboard import back_button, categoryAgent
from keyboards.inline.locationAgent import backagent
from keyboards.inline.referentagentkeyboard import Referent
from loader import dp, bot
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text_contains="agenttalab1")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    url_document = "https://uzpharmagency.uz/uploads/pages/Litsenziya/%D1%82%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%20%D0%98%D0%B7%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20.pdf"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_document, caption="<b>Dori vositalari va tibbiy buyumlarni tayyorlash faoliyati bilan shug‘ullanish uchun moddiy-texnik baza, asbob-uskunalar, texnik vositalar va xodimlarga bo‘lgan talablar</b>",reply_markup=backagent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="agenttalab2")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    url_document = "https://uzpharmagency.uz/uploads/pages/Litsenziya/%D0%A2%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BA%20%D0%BF%D1%80%D0%BE%D0%B8%D0%B7%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D1%83%201.pdf"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_document, caption="<b>Dori vositalarini ishlab chiqarish faoliyati bilan shug‘ullanish uchun moddiy-texnik baza, asbob-uskunalar, texnik vositalar va xodimlarga bo‘lgan talablar</b>",reply_markup=backagent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="agenttalab3")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    url_document = "https://uzpharmagency.uz/uploads/pages/Litsenziya/%D1%82%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20%D0%BE%D0%BF%D1%82.pdf"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_document, caption="<b>Dori vositalari va tibbiy buyumlarni ulgurji realizatsiya qilish faoliyati bilan shug‘ullanish uchun  moddiy-texnik baza, asbob-uskunalar, texnik vositalar va xodimlarga bo‘lgan talablar</b>",reply_markup=backagent)
    await call.answer(cache_time=60)



@dp.callback_query_handler(text_contains="agenttalab4")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.delete()
    await call.message.answer("Bo'limlardan birini tanlang: ", reply_markup=categoryAgent)
