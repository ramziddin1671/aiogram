import logging
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from keyboards.inline.locationKamitet import backkamitet
from loader import dp, bot
from keyboards.inline.AgentKeyboard import back_buttonkamitet, categoryKamitet
from keyboards.inline.bolinmacamitet import bolinmaKamitets
from keyboards.inline.callback_data import bolinmacamitet_callback

@dp.callback_query_handler(text="xududkamitet")
async def kamitet_xudud(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Bo'linmalardan birini tanlang 📞 (99871)203-01-01</b>", reply_markup=bolinmaKamitets)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="kamitetlaboratory")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    id_document = "BQACAgIAAxkBAAIPPGG55WEr5YYzmb_5rL1BV2fOrxWlAAJXEgAC7XrQSccQuKkfAAE9miME"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>Dori vositalari sifatini nazorat qilish va standartlashtirish laboratoriyasi</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="kamitettaksikolog")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    id_document = "BQACAgIAAxkBAAIPQmG55pTu7waVqmMvwLCHohOQiCwWAAJaEgAC7XrQSY6yZ47U-MqbIwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>Farmako-toksikologik tadqiqot laboratoriyasi</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="kamitetfarmakopea")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    id_document = "BQACAgIAAxkBAAIPRGG553UTah-N1JLmv2TICZQN-xHzAAJgEgAC7XrQSUnOeAJNg5ZUIwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>Farmakopeya qoʻmitasi</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="kamitetfarmakalogiya")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    id_document = "BQACAgIAAxkBAAIPRmG56AYgzjjcWzA75_tFHUDFJmHZAAJjEgAC7XrQSVi4V0LseEDeIwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>Farmokologiya Komiteti</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="kamitetnarkotik")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    id_document = "BQACAgIAAxkBAAIPSGG56TyjGJe5coYBh6bNZVQvg4V9AAJqEgAC7XrQSSkfVf1C-lGFIwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>Narkotik moddalarni nazorat qilish qoʻmitasi</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="kamitetpoligrafiya")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    id_document = "BQACAgIAAxkBAAIPVGG56hIZCoNjH831c8i59qdm_xpCAAJrEgAC7XrQSXzFKIN62GIhIwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>Poligrafiya bo'limi</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="kamitetqiyoslash")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    id_document = "BQACAgIAAxkBAAIPVmG56qywkTJLLmEKGwiS7dMVJXjIAAJsEgAC7XrQSUgPDjL-KssfIwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>Qiyoslash laboratoriyasi</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="kamitetRoyxat")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    id_document = "BQACAgIAAxkBAAIPWGG560I1PEZXAf4fHOlwY5nbTfr7AAJtEgAC7XrQSXte0fIKT6R3IwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>Ro'yxatga olish bo'limi</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="kamitetsifatnazorat")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    id_document = "BQACAgIAAxkBAAIPWmG569l3ZQWxIfZWJwWLHwbSNJ9fAAJvEgAC7XrQSVZqO4GFsQJxIwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>Tibbiy buyumlar va tibbiy texnika sifatini nazorat qilish laboratoriyasi</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="kamitetvaksina")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    id_document = "BQACAgIAAxkBAAIPXGG57HI4PuQjt5HQgyulpj2Mi-DEAAJxEgAC7XrQSWWLadQmMVWLIwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>Vaksinalar, sarum preparatlari va mikrobiologik tadqiqotlar laboratoriyasi</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="kamitetyangitexnika")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    id_document = "BQACAgIAAxkBAAIPXmG57SAiUaiVG9CZhRo2nrBG0L8KAAJ4EgAC7XrQSa0Kfpz362X3IwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>Yangi tibbiy texnika qo'mitasi</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="kamitetGxP")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    id_document = "BQACAgIAAxkBAAIPYGG57bOjaZCztj87yewJjJMG1ZMbAAJ8EgAC7XrQScQtIseiCk1iIwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>Zarur amaliyotlar (GxP) milliy inspektorati boʻlimi</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancelKamitet")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.delete()
    await call.message.answer("bo'limlardan birini tanlang 📞 (99871)203-01-01", reply_markup=categoryKamitet)