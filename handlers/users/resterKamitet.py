import logging

from keyboards.inline.AgentKeyboard import back_button, categoryAgent, categoryKamitet
from keyboards.inline.locationKamitet import backkamitet
from keyboards.inline.referentagentkeyboard import Referent
from keyboards.inline.resterKamitet import ResterDori, ResterYaroqsiz
from loader import dp, bot
from aiogram.types import CallbackQuery

@dp.callback_query_handler(text="resterDori")
async def kamitet_rester(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Restrlar</b> 📞 (99871)242-84-16", reply_markup=ResterDori)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="rester05_11_21")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    url_document = "BQACAgIAAxkBAAIN-GTsZZK5GyGhkVl7u4dS0KKpJbduAAIcOwACyIBgSw3tOUJ8qsevMAQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_document, caption="<b>Dori-darmonlar va tibbiy buyumlar va tibbiy texnikasining davlat reestriga O'zbekiston Respublikasi tibbiy amaliyotida foydalanish uchun tasdiqlangan 2023-yil 27-sonli qo'shimchalar (28.08.2023).\n8 ta Excel faylini o'z ichiga olgan arxiv sifatida taqdim etilgan:\n1. Mahalliy dorilar,\n2. MDH mamlakatlarida ishlab chiqarilgan dorilar,\n3. Xorijiy mamlakatlarda ishlab chiqarilgan dorilar,\n4. Dori vositalari \n5. Vivo jonli kasalliklarni aniqlash uchun dorilar \n6. Tibbiy asbob -uskunalar \n7. Tibbiy asboblar\n8. In vitro diagnostika uchun tibbiy asboblar.</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="rester21_01_21")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    url_document = "BQACAgIAAxkBAAIDaWQ5JVwLWNqazRphPf3_NpBesiqEAAJrJwACV7LJSUJFeZVvp7PWLwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_document, caption="<b>O`zbekiston Respublikasi Sog'liqni saqlash vazirligining 2023 yil 27 -sonli O'zbekiston Respublikasi tibbiyot amaliyotida foydalanishga ruxsat berilgan dori vositalari va tibbiy buyumlar va tibbiy texnikalarning davlat reestri. (O‘zbekiston Respublikasi Sog‘liqni saqlash vazirligining 'Dori vositalari, tibbiyot buyumlari va tibbiyot texnikasini ekspertiza va standartlashtirish davlat markazi' DUK ekspert kengashi majlisida chop etish uchun tavsiya etilgan (03.03.2023  4 -sonli protokol).</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="resterYaroqsiz")
async def kamitet_rester(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Restrlar</b> 📞 (99871)203-01-01", reply_markup=ResterYaroqsiz)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="resteryaroqsiz1")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    id_document = "BQACAgIAAxkBAAIDQ2Q3gQNjkZloUyNEETVN1LRcXkGiAAK1KQACZK3BSVPQivc3j03-LwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>2023 1 kv da yaroqsiz deb topilgan tibbiy mahsulotlar boʻyicha maʼlumot.</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="resteryaroqsiz2")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    id_document = "BQACAgIAAxkBAAILJGTDaMWstK1RSI-xr7xJIWFtHQZJAALOLQACWbQgSiG2Fmev1AMqLwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>2023 2 kv da yaroqsiz deb topilgan tibbiy mahsulotlar boʻyicha maʼlumot.</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="resteryaroqsiz3")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    id_document = "BQACAgIAAxkBAAIZQGVvEXE5hwwvrn69KXgBeM5YwbIlAAKwOQAC8dx4S5wr8NaTka7pMwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>2023 3 kv da yaroqsiz deb topilgan tibbiy mahsulotlar boʻyicha maʼlumot.</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancelKamitet")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.delete()
    await call.message.answer("bo'limlardan birini tanlang 📞 (99871)203-01-01", reply_markup=categoryKamitet)


@dp.callback_query_handler(text="backrester")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.delete()
    await call.message.answer("bo'limlardan birini tanlang 📞 (99871)203-01-01", reply_markup=categoryKamitet)
