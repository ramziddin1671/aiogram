from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, contact, message
from keyboards.default.menuKeyboard import menu
from keyboards.default.menuKeyboard import glav, menu
from keyboards.inline.murojatAgentlar import MurojatKarievAgent, MurojatAkbarovAgent, MurojatTemirovAgent, \
    MurojatBegmatovaAgent
from states.newpost import NewPost, KarievAgent, AkbarovAgent, TemirovAgent, BegmatovaAgent
from keyboards.inline.manage_post import confirmation_keyboard, post_callback, KarievAgent_callback, \
    KarievAgent_keyboard, AkbarovAgent_callback, AkbarovAgent_keyboard, TemirovAgent_callback, TemirovAgent_keyboard, \
    BegmatovaAgent_callback, BegmatovaAgent_keyboard
from data.config import ADMINS
from loader import dp, bot
from data.config import ADMINS
import logging
from keyboards.inline.AgentKeyboard import categoryAgent, coursesMenu, xududMenu


@dp.callback_query_handler(text_contains="bossKarievaa")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/uploads/manage/95adce426e0cd86ea353a84171ed118e.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="Farmatsevtika tarmog'ini rivojlantirish agentligi direktori\nQabul kuni: 🕰 Сhorshanba 16:00-18:00", reply_markup=MurojatKarievAgent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backKariev")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("bo'limlardan birini tanlang", reply_markup=categoryAgent)


@dp.callback_query_handler(text="murojatKariev")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await KarievAgent.NewMessage.set()


@dp.message_handler(state=KarievAgent.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await KarievAgent.next()


@dp.message_handler(state=KarievAgent.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=KarievAgent_keyboard)
    await KarievAgent.next()


@dp.callback_query_handler(KarievAgent_callback.filter(action="postKarievAgent"), state=KarievAgent.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        msg = data.get("msg")
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat yuborildi 3-ish kunida sizga aloqaga chiqilishi belgilangan", reply_markup=glav)
    await bot.send_message(35824787, f"Foydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(35824787, f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    await bot.send_message(35824787, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi shart ❗️</b>", parse_mode="HTML")


@dp.callback_query_handler(KarievAgent_callback.filter(action="cancelKarievAgent"), state=KarievAgent.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


 # 2chi raxbarga o'tildi
@dp.callback_query_handler(text_contains="bossAkbarov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/uploads/manage/fc5ff028866a61deac902343519465e4.jpg"
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer_photo(url_photo, caption="Farmatsevtika tarmog'ini rivojlantirish agentligi direktorining birinchi o‘rinbosari\nQabul kuni: 🕰 Dushanba 16:00-18:00", reply_markup=MurojatAkbarovAgent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backAkbarov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("bo'limlardan birini tanlang", reply_markup=categoryAgent)


@dp.callback_query_handler(text="murojatAkbarov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await AkbarovAgent.NewMessage.set()


@dp.message_handler(state=AkbarovAgent.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await AkbarovAgent.next()


@dp.message_handler(state=AkbarovAgent.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=AkbarovAgent_keyboard)
    await AkbarovAgent.next()


@dp.callback_query_handler(AkbarovAgent_callback.filter(action="postAkbarovAgent"), state=AkbarovAgent.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        msg = data.get("msg")
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat yuborildi 3-ish kunida sizga aloqaga chiqilishi belgilangan", reply_markup=glav)
    await bot.send_message(35824787, f"Foydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(35824787, f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    await bot.send_message(35824787, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi shart ❗️</b>", parse_mode="HTML")


@dp.callback_query_handler(AkbarovAgent_callback.filter(action="cancelAkbarovAgent"), state=AkbarovAgent.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


 # 3chi raxbarga o'tildi
@dp.callback_query_handler(text_contains="bossEshmuradov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/uploads/manage/161ded8202e5f6cd7794c09f507ea388.jpg"
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer_photo(url_photo, caption="Farmatsevtika tarmog'ini rivojlantirish agentligi direktorining o‘rinbosari\nQabul kuni: 🕰 Juma 16:00-18:00", reply_markup=MurojatTemirovAgent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backTemirov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("bo'limlardan birini tanlang", reply_markup=categoryAgent)


 # 4chi raxbarga o'tildi
@dp.callback_query_handler(text_contains="bossTemirov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/uploads/manage/38b077b839a481b389f11b9fa44034c2.jpg"
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer_photo(url_photo, caption="Farmatsevtika tarmog'ini rivojlantirish agentligi direktorining o‘rinbosari\nQabul kuni: 🕰 Seshanba 16:00-18:00", reply_markup=MurojatTemirovAgent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backTemirov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("bo'limlardan birini tanlang", reply_markup=categoryAgent)


@dp.callback_query_handler(text="murojatTemirov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await TemirovAgent.NewMessage.set()


@dp.message_handler(state=TemirovAgent.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await TemirovAgent.next()


@dp.message_handler(state=TemirovAgent.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=TemirovAgent_keyboard)
    await TemirovAgent.next()


@dp.callback_query_handler(TemirovAgent_callback.filter(action="postTemirovAgent"), state=TemirovAgent.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        msg = data.get("msg")
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat yuborildi 3-ish kunida sizga aloqaga chiqilishi belgilangan", reply_markup=glav)
    await bot.send_message(1256224042, f"Foydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(1256224042, f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    await bot.send_message(1256224042, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi shart ❗️</b>", parse_mode="HTML")


@dp.callback_query_handler(TemirovAgent_callback.filter(action="cancelTemirovAgent"), state=TemirovAgent.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


 # 4chi raxbarga o'tildi
@dp.callback_query_handler(text_contains="AgentBegmatova")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/uploads/manage/3f35a8e0201e19f47711d12dfbf753ba.jpg"
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer_photo(url_photo, caption="FARMATSEVTIKA TARMOG'INI RIVOJLANTIRISH AGENTLIGI Matbuot xizmati rahbari\nQabul kunlari: 🕰 Dushanba, chorshanba, 16:00-18:00", reply_markup=MurojatBegmatovaAgent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backBegmatova")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("bo'limlardan birini tanlang", reply_markup=categoryAgent)


@dp.callback_query_handler(text="murojatBegmatova")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await BegmatovaAgent.NewMessage.set()


@dp.message_handler(state=BegmatovaAgent.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await BegmatovaAgent.next()


@dp.message_handler(state=BegmatovaAgent.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=BegmatovaAgent_keyboard)
    await BegmatovaAgent.next()


@dp.callback_query_handler(BegmatovaAgent_callback.filter(action="postBegmatovagent"), state=BegmatovaAgent.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        msg = data.get("msg")
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat yuborildi 3-ish kunida sizga aloqaga chiqilishi belgilangan", reply_markup=glav)
    await bot.send_message(35824787, f"Foydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(35824787, f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    await bot.send_message(35824787, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi shart ❗️</b>", parse_mode="HTML")


@dp.callback_query_handler(BegmatovaAgent_callback.filter(action="cancelBegmatovaAgent"), state=BegmatovaAgent.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


@dp.message_handler(text="Bosh saxifaga")
async def select_category(message: Message):
    await message.answer(f"<b>Bo'limlardan birini tanlang</b>", reply_markup=menu)