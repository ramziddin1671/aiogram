import logging

from keyboards.inline.AgentKeyboard import back_button, categoryAgent, categoryKamitet
from keyboards.inline.Nashrlar import NashrXabarnoma, NashrDavlat
from keyboards.inline.locationKamitet import backkamitet
from keyboards.inline.referentagentkeyboard import Referent
from keyboards.inline.resterKamitet import ResterDori, ResterYaroqsiz
from loader import dp, bot
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text="xabarnomanashr")
async def kamitet_rester(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Restrlar</b> 📞 (99871)203-01-01", reply_markup=NashrXabarnoma)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="xabarnoma0")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    url_document = "BQACAgIAAxkBAAIBJmQb7eArGyLAptJfTtPgdf24mEQEAAJGJQAC4O_hSAsoYN61ql0wLwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_document, caption="<b>Oʻzbekiston farmasevtik xabarnomasi № 1-4/2022</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="xabarnoma1")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    url_document = "BQACAgIAAxkBAAICN2LqGbNX1UlPs0sAAaejXt5_l9vSsgACvRwAAlCLWEv0qXiPOXCFFykE"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_document, caption="<b>Oʻzbekiston farmasevtik xabarnomasi №1/2021</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="xabarnoma2")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    url_document = "BQACAgIAAxkBAAICOWLqGtvn4AUKXQFjs4Vi3CajwHclAAK-HAACUItYSxv4u4fDUEofKQQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_document, caption="<b>Oʻzbekiston farmasevtik xabarnomasi №2/2021</b>",
                                       reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="xabarnoma3")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    url_document = "BQACAgIAAxkBAAICO2LqG0fiNexCtwNP9GELm6sMLx66AALAHAACUItYS9Fq1ypSUFdeKQQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_document, caption="<b>Oʻzbekiston farmasevtik xabarnomasi №3-4/2021</b>",
                                       reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="xabarnoma4")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    url_document = "BQACAgIAAxkBAAISKmU_op2gm-8KH8tZGASs_6HprSHUAAJZMgACG2kBSor7uh7DkjC1MAQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_document, caption="<b>Oʻzbekiston farmasevtik xabarnomasi №1-2/2023</b>",
                                       reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="davlatnashr")
async def kamitet_rester(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Oʻzbekiston Respublikasi davlat farmakopeyasi</b> 📞 (99871)203-01-01", reply_markup=NashrDavlat)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="davlatnashr1")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    url_document = "BQACAgIAAxkBAAICNWLqFzXrz0w3u-cjc7nLotkCOf_mAALXIAACUItQS5M3UNXJWyjIKQQ"
    await call.message.delete()
    await call.message.answer("iltimos kuting!")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_document, caption="<b>O'zbekiston Respublikasi Davlat farmokopeyasi 1 - nashr 2 - jildi bo'yicha umumlashtirilgan ma'lumot</b>",
                                       reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancelKamitet")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.delete()
    await call.message.answer("bo'limlardan birini tanlang 📞 (99871)203-01-01", reply_markup=categoryKamitet)


@dp.callback_query_handler(text="backnashr")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.delete()
    await call.message.answer("Bo'limlardan birini tanlang 📞 (99871)203-01-01", reply_markup=categoryKamitet)