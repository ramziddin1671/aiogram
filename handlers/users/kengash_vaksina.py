import logging

from keyboards.inline.Vaksina_Keyboard import kengash_Vak
from keyboards.inline.locationVaksina import backvaksina
from loader import dp, bot
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text_contains="kengash1")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    id_document = "https://toshvziti.uz/media/media/%D0%90%D0%BF%D1%80%D0%BE%D0%B1%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9_%D0%A1%D0%B5%D0%BC%D0%B8%D0%BD%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%BE%D0%B2%D0%B5%D1%82_2.pdf"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>Toshkent vaktsina va zardoblar ilmiy-tadkikot instituti xuzuridagi DSc.04/04.06.2021.Tib/B.134.01 raka ivi l i ilmiy kengash raisi I.X.Mamatqulovga</b>",reply_markup=backvaksina)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="kengash2")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    id_document = "BQACAgIAAxkBAAICXGLqHjAwNDrXaPL-bwhBKsHmqQGpAAIIGwAC_wRRSzwiT277QuUCKQQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>Toshkent vaktsina va zardoblar ilmiy-tadqiqot instituti huzurida tibbiyot, biologiya fanlari boʼyicha ilmiy darajalar beruvchi DSc.04/04.06.2021 Tib/B.134.01 shifrli ilmiy kengash tuzildi.</b>",reply_markup=backvaksina)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancelvaksina")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.delete()
    await call.message.answer("Kengash a'zolari 📞 (+99871)234-77-67, 234-59-87", reply_markup=kengash_Vak)