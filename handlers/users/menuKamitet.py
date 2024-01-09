from keyboards.inline.AgentKeyboard import categoryKamitet, back_buttonkamitet
from keyboards.inline.Nashrlar import NashrKamitet
from keyboards.inline.resterKamitet import ResterKamitet
from states.personalData import PersonalData
from loader import dp, bot
import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, contact
from keyboards.inline.AgentKeyboard import bosskamitet
from keyboards.default.menuKeyboard import glav, menu
from keyboards.inline.locationKamitet import backkamitet, backkamitetxaqida
from states.newpost import NewPost, kamadmin
from keyboards.inline.manage_post import confirmation_keyboard, post_callback, admin_keyboard, admin_callback
from data.config import ADMINS


@dp.message_handler(text="DVTBTTESDM DUK")
async def kamitet(message: Message):
    await message.answer(f"<b>Bo'limlardan birini tanlang </b>📞 (99871)203-01-01", reply_markup=categoryKamitet)


@dp.callback_query_handler(text="kamitet")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.delete()
    text = f'Manzil: 100002, Toshkent sh., Ozod koʻchasi, K. Umarov tor koʻchasi, 16 uy.\n'
    text += f"Telefon raqami:+998971-203-01-01\n"
    text += f"Faks: 242-48-25. \n"
    text += f"E-mail:  farmkomitet@ssv.uz \n"
    text += f"To'liq tanishib chiqish uchun: <a href='https://uzpharm-control.uz/uz/pages/about'>Batafsil</a>  \n"
    await call.answer(cache_time=60)
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text, reply_markup=backkamitetxaqida)


@dp.callback_query_handler(text="locationKamitet")
async def kamitet_boss(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Sizni Kutib qolamiz! 😊</b> 📞 (99871)203-01-01")
    await call.answer(cache_time=60)
    await call.message.answer_location(latitude=41.32753851835419, longitude=69.2309474406898, reply_markup=backkamitet)


@dp.callback_query_handler(text="bossKamitet")
async def kamitet_boss(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Rahbarni tanlang</b> 📞 (99871)203-01-01", reply_markup=bosskamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancelKamitet")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.delete()
    await call.message.answer("bo'limlardan birini tanlang 📞 (99871)203-01-01", reply_markup=categoryKamitet)


@dp.callback_query_handler(text="searchkamitet")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni Anonim nomingiz yoki F.I.O yozgan holda qoldiring", reply_markup=ReplyKeyboardRemove())
    await kamadmin.NewMessage.set()


@dp.message_handler(state=kamadmin.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await kamadmin.next()


@dp.message_handler(state=kamadmin.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=admin_keyboard)
    await kamadmin.next()


@dp.callback_query_handler(admin_callback.filter(action="postadmin"), state=kamadmin.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        msg = data.get("msg")
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojatingiz yuborildi, 3-ish kunida sizga aloqaga chiqilishi belgilangan", reply_markup=glav)
    await bot.send_message(1256224042, f"<b>Xurmatli Admin ! Farmkamitet uchun</b>\nFoydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(1256224042, f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    await bot.send_message(1256224042, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi aytildi ❗️</b>", parse_mode="HTML")
    await bot.send_message(1066422186, f"Foydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(1066422186, f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    await bot.send_message(1066422186, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi shart ❗️</b>", parse_mode="HTML")


@dp.callback_query_handler(admin_callback.filter(action="canceladmin"), state=kamadmin.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


@dp.callback_query_handler(text="resterkamitet")
async def kamitet_rester(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Reestrlar</b> 📞 (99871)203-01-01", reply_markup=ResterKamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="nashrkamitet")
async def kamitet_rester(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Nashrlar</b> 📞 (99871)203-01-01", reply_markup=NashrKamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="xududkamitet")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    # await call.message.answer("Iltimos kuting yuborilmoqda!")
    # url = "BQACAgIAAxkBAAIDTWMPL1iSRjLZEWu-bHc8D-ttIPBCAAK0HwACdYB5SNAhHdnoEHL1KQQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("<b>Bo'limlarimiz haqidagi to'liq ma'lumotni rasmiy web-saytimizdan olishingiz mumkin. <a href='https://uzpharm-control.uz/uz/departments'>uzpharm-control.uz</a></b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.message_handler(text="Bosh saxifaga")
async def select_category(message: Message):
    await message.answer(f"<b>Bo'limlardan birini tanlang</b>", reply_markup=categoryKamitet)