import logging

from aiogram.dispatcher import FSMContext

from keyboards.default.menuKeyboard import glav
from keyboards.inline.AgentKeyboard import categoryKamitet
from keyboards.inline.Farmnadzor_komitet import Farm_nadzor
from keyboards.inline.locationKamitet import backkamitet
from keyboards.inline.manage_post import admin_keyboard, farmnadzor_keyboard, farmnadzor_callback
from loader import dp, bot
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, contact

from states.personalData import FarmnadzorData


@dp.callback_query_handler(text="FarmakonazoratKamitet")
async def kamitet_rester(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Dori vositalarini qo'llashda aniqlangan nojo'ya reaktsiyalarni xabardor qilishdagi o'rningiz\nВаша роль в сообщении о нежелательных реакциях на лекарства</b> 📞 (99871)203-01-01", reply_markup=Farm_nadzor)
    await call.answer(cache_time=60)


# @dp.callback_query_handler(text_contains="Shifokor_nadzor")
# async def buy_books(call: CallbackQuery):
#     callback_data = call.data
#     logging.info(f"{callback_data=}")
#     await call.message.answer("Iltimos kuting yuborilmoqda!")
#     url_document = "BQACAgIAAxkBAAIL8GTMhLTvkGrZNOKanH7rCgwcn2bFAAJ9LwACLupoSuky_GdZW2JXLwQ"
#     await call.message.delete()
#     # await call.message.edit_reply_markup(reply_markup=None)
#     await call.message.answer_document(url_document, caption="<b>Hurmatli shifokor ushbu xabarnomani to'ldirib quydagi manzillarga yuborishingizni so'raymiz:\n1. Elektron manzilga: farmkomitet@minzdrav.uz\n2. Telegram orqali: @ElSvech</b>",reply_markup=backkamitet)
#     await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="Shifokor_nadzor")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    id_document = "BQACAgIAAxkBAAIL-2TMhn0-uQFU8UgaMGryE45f-atoAAKENgACbQVhStKFIkDR1m5FLwQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(id_document, caption="<b>Hurmatli shifokor ushbu xabarnomani to'ldirib quydagi manzillarga yuborishingizni so'raymiz:\n1. Elektron manzilga: farmkomitet@minzdrav.uz\n2. Telegram orqali: @ElSvech</b>",reply_markup=backkamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="Bemor_nadzor")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("Hurmatli bemor Sizdan bir qancha ma'lumotlar berishingizni so'raymiz!\nIltimos bemorning Ф.И.O sini to'liq xolda yozing\nУважаемый пациент, просим Вас предоставить некоторую информацию!\nПожалуйста, напишите полный F.I.O пациента", reply_markup=ReplyKeyboardRemove())
    await FarmnadzorData.fullName.set()


@dp.message_handler(state=FarmnadzorData.fullName)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring\nОставьте нам ваш номер телефона, чтобы мы могли связаться с вами")
    await FarmnadzorData.next()


@dp.message_handler(state=FarmnadzorData.phoneNum)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Nojo'ya reaksiya bergan dorini nomini kiriting\nВведите название препарата, вызвавшего побочную реакцию")
    await FarmnadzorData.next()


@dp.message_handler(state=FarmnadzorData.dorinomi)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(dori=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Nojo'ya reaksiya ko'rinishi xaqida ma'lumot bering\nДайте информацию о появлении побочных эффектов")
    await FarmnadzorData.next()


@dp.message_handler(state=FarmnadzorData.reaktsiya_batavsil)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(reaktsiya=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Xabarni yuboraymi?",
                         reply_markup=farmnadzor_keyboard)
    await FarmnadzorData.next()


@dp.callback_query_handler(farmnadzor_callback.filter(action="postfarmnadzor_keyboard"), state=FarmnadzorData.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        msg = data.get("msg")
        dori = data.get("dori")
        reaktsiya = data.get("reaktsiya")
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojatingiz mutahasislarga yuborildi, Ma'lumotlarda xatolik bo'lmasa Tez orada siz bilan bog'lanishadi!\nВаш запрос отправлен специалистам, если в данных нет ошибок, они свяжутся с вами в ближайшее время!", reply_markup=glav)
    await bot.send_message(1256224042, f"<b>Xurmatli Admin ! Farmakanadzor uchun</b>\nFoydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(1256224042, f"<b>Bemorning ma'lumoti</b>:\n {text}\nRaqami: {msg}\n<b>Reaktsiya bergan dori nomi:</b> {dori}\n<b>Reaktsiya xaqida:</b> {reaktsiya}", parse_mode="HTML")
    await bot.send_message(1256224042, f"<b>Foydalanuvchiga 1 ish kunida javob berilishi aytildi ❗️</b>", parse_mode="HTML")
    await bot.send_message(118917174, f"Foydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(118917174, f"<b>Bemorning ma'lumoti</b>:\n {text}\nRaqami: {msg}\n<b>Reaktsiya bergan dori nomi:</b> {dori}\n<b>Reaktsiya xaqida:</b> {reaktsiya}", parse_mode="HTML")
    await bot.send_message(118917174, f"<b>Foydalanuvchiga 1 ish kunida javob berilishi shart ❗️</b>", parse_mode="HTML")
    await bot.send_message(281255341, f"Foydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(281255341, f"<b>Bemorning ma'lumoti</b>:\n {text}\nRaqami: {msg}\n<b>Reaktsiya bergan dori nomi:</b> {dori}\n<b>Reaktsiya xaqida:</b> {reaktsiya}", parse_mode="HTML")
    await bot.send_message(281255341, f"<b>Foydalanuvchiga 1 ish kunida javob berilishi shart ❗️</b>", parse_mode="HTML")


@dp.callback_query_handler(farmnadzor_callback.filter(action="cancelfarmnadzor_keyboard"), state=FarmnadzorData.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=categoryKamitet)


@dp.callback_query_handler(text="backnadzor")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.delete()
    await call.message.answer("bo'limlardan birini tanlang 📞 (99871)203-01-01", reply_markup=categoryKamitet)
