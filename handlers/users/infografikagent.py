import logging

from keyboards.inline.AgentKeyboard import categoryAgent
from keyboards.inline.locationAgent import backagent
from loader import dp, bot
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text_contains="agentdorimajburiy")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos, kuting, yuborilmoqda!")
    url_photo = "https://uzpharmagency.uz/uploads/infographics/bb51e800f0e8611f8e3f028fcc6e360e.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_photo, caption="<b>Dorixonalarda bo‘lishi majburiy bo‘lgan tibbiy buyumlar nimalardan iborat?</b>",reply_markup=backagent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="agentchek")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos, kuting, yuborilmoqda!")
    url_photo = "https://uzpharmagency.uz/uploads/infographics/f5ff1fff8d4e0964366dfaa8703800b9.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_photo, caption="<b>Dorixonada dori vositasi uchun tovar cheki berish majburiymi?</b>",reply_markup=backagent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="agentnazorat")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos, kuting, yuborilmoqda!")
    url_photo = "https://uzpharmagency.uz/uploads/infographics/dd044771e87db3f8bb88f27305ad1b27.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_photo, caption="<b>Farmatsevtika tarmog‘ini rivojlantirish agentligi Litsenziyalash va nazorat qilish boshqarmasining 2…</b>",reply_markup=backagent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="agentboshqarma")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos, kuting, yuborilmoqda!")
    url_photo = "https://uzpharmagency.uz/uploads/infographics/1f26d77364b5de79bffcedbdf36c2337.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_photo, caption="<b>Litsenziyalash va nazorat qilish boshqarmasining farmatsevtika faoliyatini (Dori vositalari va tibbi…</b>",reply_markup=backagent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="agentulgurji")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos, kuting, yuborilmoqda!")
    url_photo = "https://uzpharmagency.uz/uploads/infographics/7cd80ab92e5aba3f1466059d956ba266.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_photo, caption="<b>Ulgurji realizatsiya qiluvchi tashkilotlar dori vositalari va tibbiy buyumlarni kimlardan xarid qili…</b>",reply_markup=backagent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="agenytchakana")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos, kuting, yuborilmoqda!")
    url_photo = "https://uzpharmagency.uz/uploads/infographics/088b0eee6c145e89f5593e7eea0f211d.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_photo, caption="<b>Farmatsevtika faoliyatini (Dori vositalari va tibbiy buyumlarni chakana realizatsiya qilish bundan m…</b>",reply_markup=backagent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="agentgp")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos, kuting, yuborilmoqda!")
    url_photo = "https://uzpharmagency.uz/uploads/infographics/00a4db4f553f952e00b1a1bb6afd410c.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_photo, caption="<b>GxP - bu farmatsevtika sohasida qo‘llaniladigan va barcha ilg‘or usullar uchun umumiy atama sifatida…</b>",reply_markup=backagent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="agentyaroqsiz")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos, kuting, yuborilmoqda!")
    url_photo = "https://uzpharmagency.uz/uploads/infographics/ca356fd544707d97738fdd1c1e856f55.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_photo, caption="<b>Qo‘llash uchun yaroqsiz dori vositalari va tibbiy buyumlar ularning egalarining yoki sudning qarori …</b>",reply_markup=backagent)
    await call.answer(cache_time=60)


dp.callback_query_handler(text="cancelAgent")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.delete()
    await call.message.answer("Bo'limlardan birini tanlang: ", reply_markup=categoryAgent)