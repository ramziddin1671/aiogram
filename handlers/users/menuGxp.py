import logging

from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, contact
from keyboards.inline.AgentKeyboard import bosskamitet
from keyboards.default.menuKeyboard import glav, menu
from keyboards.inline.Zarur_Amaliyot import categoryGxp, RaxbarGxp, RestrGxp
from keyboards.inline.locationKamitet import backGxp, backbackGxp
from keyboards.inline.manage_post import AdminGxp_callback, AdminGxp_keyboard
from loader import dp, bot
from states.newpost import AgentAdmin, AdminGxp


@dp.message_handler(text="Zarur amaliyotlar markazi DUK")
async def kamitet(message: Message):
    await message.answer(f"<b>Bo'limlardan birini tanlang </b>📞 (+99871) 203-30-32", reply_markup=categoryGxp)


@dp.callback_query_handler(text="bossGxp")
async def kamitet_boss(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Rahbarni tanlang</b> 📞 (+99871) 203-30-32", reply_markup=RaxbarGxp)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancelGxp")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.delete()
    await call.message.answer("bo'limlardan birini tanlang 📞 (+99871) 203-30-32", reply_markup=categoryGxp)


@dp.callback_query_handler(text="Gxp")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.delete()
    text = f'Manzil: Toshkent sh., Yunusobod tumani, koʻch. Chingiz Aytmatov, 1-A uy.\n'
    text += f"Telefon raqamlari: (+99871) 203-30-32\n"
    text += f"E-mail:  gxp.duk@ssv.uz \n"
    text += f"To'liq tanishib chiqish uchun: <a href='https://uzpharm-gxp.uz/oz/menu/about'>Batafsil</a>  \n"
    await call.answer(cache_time=60)
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text, reply_markup=backGxp)


@dp.callback_query_handler(text="locationGxp")
async def kamitet_boss(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Sizni Kutib qolamiz! 😊  (+99871) 203-30-32</b>")
    await call.answer(cache_time=60)
    await call.message.answer_location(latitude=41.329432253919194, longitude=69.29118793965664, reply_markup=backbackGxp)


@dp.callback_query_handler(text="searchGxp")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni F.I.O yozgan holda qoldiring", reply_markup=ReplyKeyboardRemove())
    await AdminGxp.NewMessage.set()


@dp.message_handler(state=AdminGxp.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await AdminGxp.next()


@dp.message_handler(state=AdminGxp.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=AdminGxp_keyboard)
    await AdminGxp.next()


@dp.callback_query_handler(AdminGxp_callback.filter(action="postAdminGxp_keyboard"), state=AdminGxp.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        msg = data.get("msg")
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat yuborildi shaxsingiz va raqamingiz aniq kiritilgan bo'lsa 3-ish kunida sizga aloqaga chiqilishi belgilangan", reply_markup=glav)
    await bot.send_message(5409113909, f"Foydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(5409113909, f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    await bot.send_message(5409113909, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi shart ❗️</b>", parse_mode="HTML")
    await bot.send_message(1256224042, f"<b>Xurmatli Admin ! Gxp markaziga</b>\nFoydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(1256224042, f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    await bot.send_message(1256224042, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi aytildi ❗️</b>", parse_mode="HTML")


@dp.callback_query_handler(AdminGxp_callback.filter(action="cancelAdminGxp_keyboard"), state=AdminGxp.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


@dp.message_handler(text="Bosh saxifaga")
async def select_category(message: Message):
    await message.answer(f"<b>Bo'limlardan birini tanlang</b>", reply_markup=menu)


@dp.callback_query_handler(text="RestrGxp")
async def kamitet_boss(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Reestr</b> 📞 (+99871) 203-30-32", reply_markup=RestrGxp)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="TuzulmaGxp")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    url_document = "BQACAgIAAxkBAAICbmLqZulAsQkyA49-P6eOfM98wjSXAAKrGgACK0BRS3mHp89plitgKQQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_document, caption="<b>«Zarur amaliyotlar markazi» DUK TUZILMASI</b> 📞 (+99871) 203-30-32",reply_markup=backbackGxp)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="bolinmaGxp")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.answer("Iltimos kuting yuborilmoqda!")
    url_document = "BQACAgIAAxkBAAICgGL1NWkRXFuklT62uWkR1k3RaXEWAAJFGwAC3XWoS_F_2LVXFtGHKQQ"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_document(url_document, caption="<b>«Zarur amaliyotlar markazi» DUK Bo'linmalari</b> 📞 (+99871) 203-30-32",reply_markup=backbackGxp)
    await call.answer(cache_time=60)