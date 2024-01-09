from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, contact, message
from keyboards.default.menuKeyboard import menu
from keyboards.default.menuKeyboard import glav, menu
from states.newpost import NewPost, Newnew, kamKariev, kaminayatov, AzizovKam, MusaevKam, XasanovKam, AchilovKam, \
    BoltaboevaKam, SalievaKam, AbduraxmonovKam
from keyboards.inline.manage_post import confirmation_keyboard, post_callback, test_keyboard, test_callback, \
    kar_keyboard, kar_callback, innayatov_keyboard, innayatov_callback, AzizovKam_keyboard, AzizovKam_callback, \
    MusaevKam_callback, XasanovKam_keyboard, XasanovKam_callback, AchilovKam_callback, AchilovKam_keyboard, \
    BoltaboevaKam_callback, BoltaboevaKam_keyboard, SalievaKam_callback, SalievaKam_keyboard, AbduraxmonovKam_callback, \
    AbduraxmonovKam_keyboard
from data.config import ADMINS
from loader import dp, bot
from data.config import ADMINS
import logging
from keyboards.inline.AgentKeyboard import categoryAgent, coursesMenu, xududMenu, categoryKamitet, bosskamitet
from keyboards.inline.murojatKamitetlar import MurojatKamitet, murojatSaidov, murojatInayatov, murojatAzizov, \
    murojatMusaev, murojatXasanov, murojatAchilov, murojatBoltaboeva, murojatSalieva, murojatAbduraxmonov


@dp.callback_query_handler(text_contains="kamitetKariev")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharm-control.uz/uploads/leadership/2477971695037410.jpeg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Nartayev Agzam Orumbayevich\n'FARMATSEVTIKA MAHSULOTLARI XAVFSIZLIGI MARKAZI DIREKTORI'</b>\nQabul kuni: 🕰 Juma 16:00-18:00",reply_markup=MurojatKamitet)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backKamKariev")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("bo'limlardan birini tanlang", reply_markup=bosskamitet)


@dp.callback_query_handler(text="murojatKamKariev")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await kamKariev.NewMessage.set()


@dp.message_handler(state=kamKariev.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await kamKariev.next()


@dp.message_handler(state=kamKariev.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=kar_keyboard)
    await kamKariev.next()


@dp.callback_query_handler(kar_callback.filter(action="postKariev"), state=kamKariev.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        msg = data.get("msg")
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat yuborildi 3-ish kunida sizga aloqaga chiqilishi belgilangan", reply_markup=glav)
    await bot.send_message(35824787, text=f"Foydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(35824787, text=f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    await bot.send_message(35824787, text=f"<b>Foydalanuvchiga 3 ish kunida javob berilishi shart ❗️</b>", parse_mode="HTML")


@dp.callback_query_handler(kar_callback.filter(action="cancelKariev"), state=kamKariev.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


#2chi raxbar
@dp.callback_query_handler(text_contains="kamitetInoyatov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharm-control.uz/uploads/leadership/noimg.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Vasiyev Shoyadbek Zyadbekovich\n'Iqtisodiyot va moliya ishlari boʼyicha direktor oʼrinbosari'</b>\nQabul kuni: 🕰 ",reply_markup=murojatInayatov)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backKamitetinayatov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("bo'limlardan birini tanlang", reply_markup=bosskamitet)


@dp.callback_query_handler(text="murojatKamitetinayatov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await kaminayatov.NewMessage.set()


@dp.message_handler(state=kaminayatov.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await kaminayatov.next()


@dp.message_handler(state=kaminayatov.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=innayatov_keyboard)
    await kaminayatov.next()


@dp.callback_query_handler(innayatov_callback.filter(action="postinayatov"), state=kaminayatov.Confirm)
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


@dp.callback_query_handler(innayatov_callback.filter(action="cancelinayatov"), state=kaminayatov.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


#3chi raxbar
@dp.callback_query_handler(text_contains="kamitetTemirov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharm-control.uz/uploads/leadership/7054851691034752.jpeg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Temirov Alisher Smatillayevich\n'Farmatsevtika mahsulotlari xavfsizligi bo'yicha direktor oʼrinbosari'</b>\nQabul kuni: 🕰 Dushanba va Chorshanba 15:30-17:30",reply_markup=murojatSaidov)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="testbackKamitet")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("bo'limlardan birini tanlang", reply_markup=bosskamitet)


@dp.callback_query_handler(text="testmurojatKamitet")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await Newnew.NewMessage.set()


@dp.message_handler(state=Newnew.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await Newnew.next()


@dp.message_handler(state=Newnew.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=test_keyboard)
    await Newnew.next()


@dp.callback_query_handler(test_callback.filter(action="chop"), state=Newnew.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        msg = data.get("msg")
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat yuborildi 3-ish kunida sizga aloqaga chiqilishi belgilangan", reply_markup=glav)
    await bot.send_message(1256224042, text=f"Foydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(1256224042, text=f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    await bot.send_message(1256224042, text=f"<b>Foydalanuvchiga 3 ish kunida javob berilishi shart ❗️</b>", parse_mode="HTML")


@dp.callback_query_handler(test_callback.filter(action="qayt"), state=Newnew.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


#4chi raxbar
@dp.callback_query_handler(text_contains="kamitetMusaev")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharm-control.uz/uploads/leadership/3103421658302745.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Musaev Nodirbek Dilshodovich\n'Direktor o'rinbosari'</b>\nQabul kuni: 🕰 Dushanba - Juma 08:30-16:30",reply_markup=murojatAzizov)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backKamitetazizov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("bo'limlardan birini tanlang", reply_markup=bosskamitet)


@dp.callback_query_handler(text="murojatKamitetazizov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await AzizovKam.NewMessage.set()


@dp.message_handler(state=AzizovKam.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await AzizovKam.next()


@dp.message_handler(state=AzizovKam.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=AzizovKam_keyboard)
    await AzizovKam.next()


@dp.callback_query_handler(AzizovKam_callback.filter(action="postAzizov"), state=AzizovKam.Confirm)
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


@dp.callback_query_handler(AzizovKam_callback.filter(action="cancelAzizov"), state=AzizovKam.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


#5chi raxbar
@dp.callback_query_handler(text_contains="kamitetMusaev")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharm-control.uz/uploads/leadership/1176511637411453.jpeg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Musaev Nodirbek Dilshodovich\n'Фармакопея қўмита раиси'</b>\nQabul kunlari: 🕰 Dushanba - Juma 08:30-16:30")#,reply_markup=murojatMusaev)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backKamitetmusaev")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("bo'limlardan birini tanlang", reply_markup=bosskamitet)


@dp.callback_query_handler(text="murojatKamitetmusaev")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await MusaevKam.NewMessage.set()


@dp.message_handler(state=MusaevKam.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await MusaevKam.next()


@dp.message_handler(state=MusaevKam.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=confirmation_keyboard)
    await MusaevKam.next()


@dp.callback_query_handler(MusaevKam_callback.filter(action="post"), state=MusaevKam.Confirm)
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


@dp.callback_query_handler(MusaevKam_callback.filter(action="cancel"), state=MusaevKam.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


#6chi raxbar
@dp.callback_query_handler(text_contains="kamitetAbduraxmonov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharm-control.uz/uploads/leadership/9346801639564487.jpeg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Abduraxmonov Baxrom Sunnatovich\n'ДУК Янги тиббий техника қўмитаси раиси'</b>\nQabul kunlari: 🕰 Dushanba - Juma 08:30-16:30")#,reply_markup=murojatAbduraxmonov)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backKamitetAbduraxmonov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("bo'limlardan birini tanlang", reply_markup=bosskamitet)


@dp.callback_query_handler(text="murojatKamitetAbduraxmonov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await AbduraxmonovKam.NewMessage.set()


@dp.message_handler(state=AbduraxmonovKam.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await AbduraxmonovKam.next()


@dp.message_handler(state=AbduraxmonovKam.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=AbduraxmonovKam_keyboard)
    await AbduraxmonovKam.next()


@dp.callback_query_handler(AbduraxmonovKam_callback.filter(action="postAbduraxmonov"), state=AbduraxmonovKam.Confirm)
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


@dp.callback_query_handler(AbduraxmonovKam_callback.filter(action="cancelAbduraxmonov"), state=AbduraxmonovKam.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)



#7chi raxbar
@dp.callback_query_handler(text_contains="kamitetXasanov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharm-control.uz/uploads/leadership/4405211638863275.jpeg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Xasanov Dilshodbek Numanovich\n'Тиббий буюмлар ва тиббий техника сифатини назорат қилиш'</b>\nQabul kunlari: 🕰 Dushanba - Juma 08:30-16:30")#,reply_markup=murojatXasanov)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backKamitetxasanov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("bo'limlardan birini tanlang", reply_markup=bosskamitet)


@dp.callback_query_handler(text="murojatKamitetxasanov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await XasanovKam.NewMessage.set()


@dp.message_handler(state=XasanovKam.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await XasanovKam.next()


@dp.message_handler(state=XasanovKam.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=XasanovKam_keyboard)
    await XasanovKam.next()


@dp.callback_query_handler(XasanovKam_callback.filter(action="postXasanov"), state=XasanovKam.Confirm)
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


@dp.callback_query_handler(XasanovKam_callback.filter(action="cancelXasanov"), state=XasanovKam.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


#8chi raxbar
@dp.callback_query_handler(text_contains="kamitetАчилов")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharm-control.uz/uploads/leadership/9046121639041539.jpeg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Ачилов Абдурахим Махамадрасулович\n'Ахборот технoлогиялари бўлими бошлиғи'</b>\nQabul kunlari: 🕰 Dushanba - Juma 08:30-16:30")#,reply_markup=murojatAchilov)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backKamitetachilov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("bo'limlardan birini tanlang", reply_markup=bosskamitet)


@dp.callback_query_handler(text="murojatKamitetachilov")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await AchilovKam.NewMessage.set()


@dp.message_handler(state=AchilovKam.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await AchilovKam.next()


@dp.message_handler(state=AchilovKam.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=AchilovKam_keyboard)
    await AchilovKam.next()


@dp.callback_query_handler(AchilovKam_callback.filter(action="postAchilov"), state=AchilovKam.Confirm)
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


@dp.callback_query_handler(AchilovKam_callback.filter(action="cancelAchilov"), state=AchilovKam.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


#9chi raxbar
@dp.callback_query_handler(text_contains="kamitetBoltaboevna")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharm-control.uz/uploads/leadership/6417731638863639.jpeg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Boltaboeva Gulchexra Erkinovna\n'Дори воситалари сифатини назорат қилиш ва стандартлаштириш'</b>\nQabul kunlari: 🕰 Dushanba - Juma 08:30-16:30")#,reply_markup=murojatBoltaboeva)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backKamitetboltaboeva")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("bo'limlardan birini tanlang", reply_markup=bosskamitet)


@dp.callback_query_handler(text="murojatKamitetboltaboeva")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await BoltaboevaKam.NewMessage.set()


@dp.message_handler(state=BoltaboevaKam.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await BoltaboevaKam.next()


@dp.message_handler(state=BoltaboevaKam.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=BoltaboevaKam_keyboard)
    await BoltaboevaKam.next()


@dp.callback_query_handler(BoltaboevaKam_callback.filter(action="postBoltaboeva"), state=BoltaboevaKam.Confirm)
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


@dp.callback_query_handler(BoltaboevaKam_callback.filter(action="cancelBoltaboeva"), state=BoltaboevaKam.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


# 10chi raxbar
@dp.callback_query_handler(text_contains="kamitetSalieva")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharm-control.uz/uploads/leadership/6603881638860779.jpeg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo,
                                    caption="<b>Salieva Gulnoza Valievna\n'ДУК Рўйхатдан ўтказиш бўлими в.в.б. бошлиғи'</b>\nQabul kunlari: 🕰 Dushanba - Juma 08:30-16:30")#,reply_markup=murojatSalieva)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="backKamitetsalieva")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("bo'limlardan birini tanlang", reply_markup=bosskamitet)


@dp.callback_query_handler(text="murojatKamitetsalieva")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await SalievaKam.NewMessage.set()


@dp.message_handler(state=SalievaKam.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await SalievaKam.next()


@dp.message_handler(state=SalievaKam.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=SalievaKam_keyboard)
    await SalievaKam.next()


@dp.callback_query_handler(SalievaKam_callback.filter(action="postSalieva"), state=SalievaKam.Confirm)
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
    await bot.send_message(1256224042, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi shart ❗️</b>",
                           parse_mode="HTML")
    await bot.send_message(35824787, f"Foydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(35824787, f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\nKimga: Salieva Gulnoza Valievnaga", parse_mode="HTML")
    await bot.send_message(35824787, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi shart ❗️</b>",
                           parse_mode="HTML")


@dp.callback_query_handler(SalievaKam_callback.filter(action="cancelSalieva"), state=SalievaKam.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


@dp.message_handler(text="Bosh saxifaga")
async def select_category(message: Message):
    await message.answer(f"<b>Bo'limlardan birini tanlang</b>", reply_markup=menu)
