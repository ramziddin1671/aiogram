from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, contact
from keyboards.default.menuKeyboard import menu
from keyboards.default.menuKeyboard import glav, menu
from keyboards.inline.infografikakeyboard import infograficagent
from keyboards.inline.litsenziyaAgent import litsenziyalashagent
from keyboards.inline.locationAgent import backagent, backagentxaqida
from keyboards.inline.referentagentkeyboard import Referent
from states.newpost import NewPost, AgentAdmin
from keyboards.inline.manage_post import confirmation_keyboard, post_callback, AgentAdmin_keyboard, agentadmin_callback
from data.config import ADMINS
from loader import dp, bot
from data.config import ADMINS
import logging
from keyboards.inline.AgentKeyboard import categoryAgent, coursesMenu, xududMenu


@dp.message_handler(text_contains="FTRA")
async def select_category(message: Message):
    await message.answer(f"<b>Bo'limlardan birini tanlang </b> 📞 (99871)203-81-81", reply_markup=categoryAgent)


@dp.callback_query_handler(text="locationAgent")
async def kamitet_boss(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Sizni Kutib qolamiz! 😊</b>")
    await call.answer(cache_time=60)
    await call.message.answer_location(latitude=41.329432253919194, longitude=69.29118793965664, reply_markup=backagent)


@dp.callback_query_handler(text="agent")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    text = f"<b>O‘zbekiston Respublikasi Sog‘liqni saqlash vazirligi huzuridagi Farmatsevtika tarmog‘ini rivojlantirish agentligi</b> Farmatsevtika faoliyatini rivojlantirish uchun shart-sharoitlarni yaxshilash, aholi va sog‘liqni saqlash muassasalarining arzon, sifatli dori vositalari, tibbiyot buyumlari va tibbiyot texnikalari bilan taʼminlanganlik darajasini yana-da oshirish, ularning ishlab chiqarilishi, olib kirilishi va sotilishini muvofiqlashtirishning yagona tizimini joriy etish maqsadida, O‘zbekiston Respublikasi Prezidentining 2017 yil 7 noyabridagi “Farmatsevtika tarmog‘ini boshqarish tizimini tubdan takomillashtirish chora-tadbirlari to‘g‘risidagi” 5229-son Farmoniga muvofiq, O‘zbekiston Respublikasi Sog‘liqni saqlash vazirligi huzurida Farmatsevtika tarmog‘ini rivojlantirish Agentligi tashkil etildi.\n"
    text += f"<b>Bizning manzil</b>: O'zbekiston Respublikasi, Toshkent shahar, 100084,Chingiz Aytmatov ko'chasi, 1A\n"
    text += f"<b>Telefon raqami</b>: +998 (71) 203-81-81\n"
    text += f"<b>To'liq tanishib chiqish uchun</b>: <a href='https://uzpharmagency.uz/oz/menu/ob-agentstve'>Batafsil</a>  \n"
    await call.message.answer(text, reply_markup=backagentxaqida)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="searchagent")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer("To'liq mazmundagi so'rovingizni F.I.O yozgan holda qoldiring", reply_markup=ReplyKeyboardRemove())
    await AgentAdmin.NewMessage.set()


@dp.message_handler(state=AgentAdmin.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await AgentAdmin.next()


@dp.message_handler(state=AgentAdmin.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=AgentAdmin_keyboard)
    await AgentAdmin.next()


@dp.callback_query_handler(agentadmin_callback.filter(action="postAgent"), state=AgentAdmin.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        msg = data.get("msg")
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat yuborildi shaxsingiz va raqamingiz aniq kiritilgan bo'lsa 3-ish kunida sizga aloqaga chiqilishi belgilangan", reply_markup=glav)
    await bot.send_message(5381890673, f"Foydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(5381890673, f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    await bot.send_message(5381890673, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi shart ❗️</b>", parse_mode="HTML")
    await bot.send_message(1256224042, f"<b>Xurmatli Admin ! Agentlik uchun</b>\nFoydalanuvchi: {mention} quyidagi murojatni yubordi:")
    await bot.send_message(1256224042, f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    await bot.send_message(1256224042, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi aytildi ❗️</b>", parse_mode="HTML")



@dp.callback_query_handler(agentadmin_callback.filter(action="cancelAgentadmin"), state=AgentAdmin.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)


@dp.message_handler(text="Bosh saxifaga")
async def select_category(message: Message):
    await message.answer(f"<b>Bo'limlardan birini tanlang</b>", reply_markup=menu)



@dp.callback_query_handler(text="boss")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("<b>Rahbarni tanlang</b> 📞 (99871)203-81-81", reply_markup=coursesMenu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="agentxudud")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("<b>Hududiy bo‘linmalar</b> 📞 (99871)203-81-81", reply_markup=xududMenu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancelAgent")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.delete()
    await call.message.answer("Bo'limlardan birini tanlang: 📞 (99871)203-81-81 ", reply_markup=categoryAgent)


@dp.callback_query_handler(text="referentagent")
async def kamitet_boss(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer(f" <b> Referent narxlar bo'yicha: </b> 📞 (99871)203-81-81", reply_markup=Referent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="infoagent")
async def info(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer(f" <b> Infografika: </b> 📞 (99871)203-81-81", reply_markup=infograficagent)
    await call.answer(cache_time=60)



@dp.callback_query_handler(text="litsenziyaagent")
async def info(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer(f" <b> Litsenziyalash </b> 📞 (99871)203-81-81", reply_markup=litsenziyalashagent)
    await call.answer(cache_time=60)





