from keyboards.default.menuKeyboard import glav
from keyboards.inline.Vaksina_Keyboard import categoryVaksina, vaksinaRaxbar, product_Vak, kengash_Vak
from keyboards.inline.locationVaksina import backlocationvaksina, backvaksina
from keyboards.inline.manage_post import admin_callback, admin_keyboard, Ashurov_Vaksina_callback, \
    Ashurov_Vaksina_keyboard
from loader import dp, bot
import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, contact

from states.newpost import kamadmin, AshurovVaksina


@dp.message_handler(text="ToshVZITI")
async def kamitet(message: Message):
    await message.answer(f"<b>Bo'limlardan birini tanlang </b>📞 (99871)234 77 67", reply_markup=categoryVaksina)


@dp.callback_query_handler(text="UnVaksina")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.delete()
    text = f"Manzil: O'zbekiston, 100084, Toshkent, Yunusobod tumani, Chingiz Aytmatov ko'chasi, 37 mo'ljal: 5-stomatologiya\n"
    text += f"Telefon raqami: (+99871) 234-77-67, 234-59-87\n"
    text += f"Faks: (+99871) 234-59-87 \n"
    text += f"E-mail: tashrivs@umail.uz \n"
    text += f"To'liq tanishib chiqish uchun: <a href='https://toshvziti.uz/uz/about/'>Batafsil</a>  \n"
    await call.answer(cache_time=60)
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text, reply_markup=backlocationvaksina)


@dp.callback_query_handler(text="locationVaksina")
async def kamitet_boss(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Sizni Kutib qolamiz! 😊</b> 📞 (+99871)234-77-67, 234-59-87")
    await call.answer(cache_time=60)
    await call.message.answer_location(latitude=41.33394190695675, longitude=69.29067508465978, reply_markup=backvaksina)


@dp.callback_query_handler(text="bossVaksina")
async def kamitet_boss(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Rahbarni tanlang</b> 📞 (+99871)234-77-67, 234-59-87", reply_markup=vaksinaRaxbar)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancelvaksina")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.delete()
    await call.message.answer("bo'limlardan birini tanlang 📞 (+99871)234-77-67, 234-59-87", reply_markup=categoryVaksina)


@dp.callback_query_handler(text="searchvak")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni F.I.O yozgan holda qoldiring", reply_markup=ReplyKeyboardRemove())
    await AshurovVaksina.NewMessage.set()


@dp.message_handler(state=AshurovVaksina.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await AshurovVaksina.next()


@dp.message_handler(state=AshurovVaksina.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=Ashurov_Vaksina_keyboard)
    await AshurovVaksina.next()


@dp.callback_query_handler(Ashurov_Vaksina_callback.filter(action="postAshurov_vaksina"), state=AshurovVaksina.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        msg = data.get("msg")
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat yuborildi shahsingiz va raqamingiz aniq kiritilgan bo'lsa 3-ish kunida sizga aloqaga chiqilishi belgilangan", reply_markup=glav)
    await bot.send_message(1256224042, f"<b>Xurmatli Admin !</b>\nFoydalanuvchi: {mention} Vaktsina zardoblash institutiga quyidagi murojatni yubordi:")
    await bot.send_message(1256224042, f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    await bot.send_message(1256224042, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi aytildi ❗️</b>", parse_mode="HTML")
    await bot.send_message(5405205576, f"Foydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(5405205576, f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    await bot.send_message(5405205576, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi shart ❗️</b>", parse_mode="HTML")


@dp.callback_query_handler(Ashurov_Vaksina_callback.filter(action="cancelAshurov_vaksina"), state=AshurovVaksina.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


@dp.callback_query_handler(text="VaksinaProduct")
async def kamitet_boss(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Mahsulot tanlang</b> 📞 (+99871)234-77-67, 234-59-87", reply_markup=product_Vak)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="VaksinaKengash")
async def kamitet_boss(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Ilmiy Kengash</b> 📞 (+99871)234-77-67, 234-59-87", reply_markup=kengash_Vak)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="cancelvaksina")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.delete()
    await call.message.answer("bo'limlardan birini tanlang 📞 (+99871)234-77-67, 234-59-87", reply_markup=categoryVaksina)
