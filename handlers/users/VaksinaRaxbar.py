from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ReplyKeyboardRemove, Message

from keyboards.default.menuKeyboard import glav
from keyboards.inline.Vaksina_Keyboard import vaksinaRaxbar, categoryVaksina
from keyboards.inline.manage_post import Ashurov_Vaksina_keyboard, Ashurov_Vaksina_callback, \
    Mamatqulov_Vaksina_keyboard, Mamatqulov_Vaksina_callback, Maxmudjonova_Vaksina_keyboard, \
    Maxmudjonova_Vaksina_callback, Dadajonov_Vaksina_keyboard, Dadajonov_Vaksina_callback, Asadulaev_Vaksina_keyboard, \
    Asadulaev_Vaksina_callback
from keyboards.inline.murojat_vaksinalar import MurojatAshurov, MurojatMamatqulov, MurojatMaxmudjonova, \
    MurojatDadajonov, MurojatAsadulaev
from loader import dp, bot
from data.config import ADMINS
import logging

from states.newpost import AshurovVaksina, MamatqulovVaksina, MaxmudjonovaVaksina, DadajonovVaksina, AsadulaevVaksina


@dp.callback_query_handler(text_contains="vaksinaAshurov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://toshvziti.uz/media/images/photo_2021-12-13_15-43-16.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="АSHUROV АBDURАXMON АKBАRАLIEVICH\nToshkent vaktsina va zardoblar ilmiy-tadqiqot instituti direktori\nQabul kunlari: 🕰 Dushanba-Juma 9:00 dan 18:00 gacha",reply_markup=MurojatAshurov)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backbossvaksina")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("Raxbariyat 📞 (+99871)234-77-67, 234-59-87", reply_markup=vaksinaRaxbar)


@dp.callback_query_handler(text="murojatAshurov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
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
    await call.message.answer("Murojat yuborildi 3-ish kunida sizga aloqaga chiqilishi belgilangan", reply_markup=glav)
    await bot.send_message(1256224042, f"Foydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(1256224042, f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    await bot.send_message(1256224042, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi shart ❗️</b>", parse_mode="HTML")


@dp.callback_query_handler(Ashurov_Vaksina_callback.filter(action="cancelAshurov_vaksina"), state=AshurovVaksina.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)

# 2 chi raxbar

@dp.callback_query_handler(text_contains="vaksinaMamatqulov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://toshvziti.uz/media/images/photo_2021-12-13_15-42-59.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="MАMАTQULOV IBROXIM XOMIDOVICH\nToshkent vaktsina va zardoblar ilmiy-tadqiqot Institut direktorining ilmiy ishlar boʼyicha oʼrinbosari\nQabul kunlari: 🕰 Dushanba-Juma 9:00 dan 18:00 gacha",reply_markup=MurojatMamatqulov)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backbossvaksina")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("Raxbariyat 📞 (+99871)234-77-67, 234-59-87", reply_markup=vaksinaRaxbar)


@dp.callback_query_handler(text="murojatMamatqulov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await MamatqulovVaksina.NewMessage.set()


@dp.message_handler(state=MamatqulovVaksina.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await MamatqulovVaksina.next()


@dp.message_handler(state=MamatqulovVaksina.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=Mamatqulov_Vaksina_keyboard)
    await MamatqulovVaksina.next()


@dp.callback_query_handler(Mamatqulov_Vaksina_callback.filter(action="postMamatqulov_vaksina"), state=MamatqulovVaksina.Confirm)
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


@dp.callback_query_handler(Mamatqulov_Vaksina_callback.filter(action="cancelMamatqulov_vaksina"), state=MamatqulovVaksina.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


# 3 chi raxbar

@dp.callback_query_handler(text_contains="vaksinaMaxmudjonova")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://toshvziti.uz/media/images/photo_2021-12-13_15-42-16.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="MАXMUDJАNOVА KOMILА SULTONOVNА\nToshkent vaktsina va zardoblar ilmiy-tadqiqot Institut Ilmiy kotibi\nQabul kunlari: 🕰 Dushanba-Juma 9:00 dan 18:00 gacha",reply_markup=MurojatMaxmudjonova)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backbossvaksina")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("Raxbariyat 📞 (+99871)234-77-67, 234-59-87", reply_markup=vaksinaRaxbar)


@dp.callback_query_handler(text="murojatMaxmudjonova")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await MaxmudjonovaVaksina.NewMessage.set()


@dp.message_handler(state=MaxmudjonovaVaksina.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await MaxmudjonovaVaksina.next()


@dp.message_handler(state=MaxmudjonovaVaksina.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=Maxmudjonova_Vaksina_keyboard)
    await MaxmudjonovaVaksina.next()


@dp.callback_query_handler(Maxmudjonova_Vaksina_callback.filter(action="postMaxmudjonova_vaksina"), state=MaxmudjonovaVaksina.Confirm)
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


@dp.callback_query_handler(Maxmudjonova_Vaksina_callback.filter(action="cancelMaxmudjonova_vaksina"), state=MaxmudjonovaVaksina.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


# 4 chi raxbar

@dp.callback_query_handler(text_contains="vaksinaDadajonov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://toshvziti.uz/media/images/photo_2022-06-06_14-42-12.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="BEKNАZOV ORIFJON NORBАEVICH\nToshkent vaktsina va zardoblar ilmiy-tadqiqot Institut direktorining umumiy ishlar boʼyicha oʼrinbosari\nQabul kunlari: 🕰 Dushanba-Juma 9:00 dan 18:00 gacha",reply_markup=MurojatDadajonov)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backbossvaksina")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("Raxbariyat 📞 (+99871)234-77-67, 234-59-87", reply_markup=vaksinaRaxbar)


@dp.callback_query_handler(text="murojatDadajonov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await DadajonovVaksina.NewMessage.set()


@dp.message_handler(state=DadajonovVaksina.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await DadajonovVaksina.next()


@dp.message_handler(state=DadajonovVaksina.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=Dadajonov_Vaksina_keyboard)
    await DadajonovVaksina.next()


@dp.callback_query_handler(Dadajonov_Vaksina_callback.filter(action="postDadajonov_vaksina"), state=DadajonovVaksina.Confirm)
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


@dp.callback_query_handler(Dadajonov_Vaksina_callback.filter(action="cancelDadajonov_vaksina"), state=DadajonovVaksina.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


# 5 chi raxbar

@dp.callback_query_handler(text_contains="kamitetAssadulaev")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://toshvziti.uz/media/images/photo_2021-12-13_15-43-06.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="АSАDULLАEV NURIDDIN SHАMSIDDINOVICH\nToshkent vaktsina va zardoblar ilmiy-tadqiqot Institut bosh hisobchisi\nQabul kunlari: 🕰 Dushanba-Juma 9:00 dan 18:00 gacha",reply_markup=MurojatAsadulaev)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backbossvaksina")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("Raxbariyat 📞 (+99871)234-77-67, 234-59-87", reply_markup=vaksinaRaxbar)


@dp.callback_query_handler(text="murojatAsadulaev")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await AsadulaevVaksina.NewMessage.set()


@dp.message_handler(state=AsadulaevVaksina.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await AsadulaevVaksina.next()


@dp.message_handler(state=AsadulaevVaksina.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=Asadulaev_Vaksina_keyboard)
    await AsadulaevVaksina.next()


@dp.callback_query_handler(Asadulaev_Vaksina_callback.filter(action="postAsadulaev_vaksina"), state=AsadulaevVaksina.Confirm)
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


@dp.callback_query_handler(Asadulaev_Vaksina_callback.filter(action="cancelAsadulaev_vaksina"), state=AsadulaevVaksina.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


@dp.callback_query_handler(text="cancelvaksina")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("Bo'limlardan birini tanlang! 📞 (+99871)234-77-67, 234-59-87", reply_markup=categoryVaksina)