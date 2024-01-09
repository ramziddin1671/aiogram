from aiogram import types
from aiogram.types import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import CallbackQuery, ReplyKeyboardRemove, Message, message

from keyboards.default.menuKeyboard import glav
from keyboards.inline.manage_post import adminbot_keyboard, Adminbot_callback
from loader import dp, bot
from filters.private_chat import IsPrivate

# @dp.message_handlers(Commands=['Til','vaqt']) Hohishga qarab 2 ta kamanda xam iwlaydi
from states.newpost import kamadmin, AdminPost
import logging

admins = [1256224042]

@dp.message_handler(IsPrivate(), Command(['til','vaqt']))
async def changeLanguage(message: types.Message):
    await message.answer(f"Til o'zgardi")


@dp.message_handler(Command(['admin']))
async def buy_courses(message: Message):
    #callback_data = call.data
    #logging.info(f"{callback_data=}")
    #logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    #await call.message.delete()
    #await call.answer(cache_time=60)
    await message.answer("Siz Admin uchun xabar jo'natmoqdasiz, Agarda sizga bot qaysidir joyda habar yubormagan bo'lsa, yoki murojat yo'llagan taqdiringizda 3 ish kunida ham javob kelmasa to'liq mazmunda so'rovingizni yuboring.\nBiz muamoni tez fursatda hal qilamiz.\nIltimos Admin uchun so'rov yuborishda quyidagilarni to'diring.")
    await message.answer("<b>To'liq mazmundagi so'rovingizni F.I.O yozgan holda qoldiring</b>", reply_markup=ReplyKeyboardRemove())
    await AdminPost.NewMessage.set()


@dp.message_handler(state=AdminPost.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Bog'lanishimiz uchun bizga telefon raqamingizni qoldiring")
    await AdminPost.next()


@dp.message_handler(state=AdminPost.Phone)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(msg=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Murojatni yuboraymi?",
                         reply_markup=adminbot_keyboard)
    await AdminPost.next()

def ReplyButton(user_id):
    button = InlineKeyboardMarkup(row_width=1)
    button.insert(InlineKeyboardButton(text='Javob berish', callback_data=f'reply_client:{user_id}'))
    return button

@dp.callback_query_handler(Adminbot_callback.filter(action="postadminbot_keyboard"), state=AdminPost.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        murojat = data.get("text")
        msg = data.get("msg")
        mention = data.get("mention")
    await state.finish()
    #await call.message.edit_reply_markup()
    await call.message.answer("Murojat yuborildi shaxsingiz va raqamingiz aniq kiritilgan bo'lsa 3-ish kunida sizga aloqaga chiqilishi belgilangan", reply_markup=glav)
    text = f"<b>Xurmatli Admin ! Admin uchun</b>\nFoydalanuvchi: {mention} quyidagi murojatni yubordi:\n\n"
    text += f"<b>Murojatning mazmuni</b>:\n {murojat}\n\n"
    text += f"<b>Raqami: </b>\n{msg}\n"
    text += f"<b>Foydalanuvchiga 3 ish kunida javob berilishi aytildi ❗️</b>"

    for admin in admins:
        await bot.send_message(chat_id=admin, text=text, reply_markup=ReplyButton(call.from_user.id))
    #await bot.send_message(1256224042, f"<b>Xurmatli Admin ! Admin uchun</b>\nFoydalanuvchi: {mention} quyidagi murojatni yubordi:")
    #await bot.send_message(1256224042, f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    #await bot.send_message(1256224042, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi aytildi ❗️</b>", parse_mode="HTML")
    #await bot.send_message(35824787, f"Foydalanuvchi: {mention} quyidagi murojatni yubordi:")
    #await bot.send_message(35824787, f"<b>Murojatning mazmuni</b>:\n {text}\nRaqami: {msg}\n", parse_mode="HTML")
    #await bot.send_message(35824787, f"<b>Foydalanuvchiga 3 ish kunida javob berilishi shart ❗️</b>", parse_mode="HTML")

@dp.callback_query_handler(text_contains='reply_client')
async def reply_client(call: CallbackQuery, state: FSMContext):
    await state.update_data({'client_id':call.data.rsplit((':'))[1]})
    await call.message.answer(text='Javob matnni kiriting: ')
    await AdminPost.Reply.set()

@dp.message_handler(state=AdminPost.Reply)
async def reply(message: Message, state: FSMContext):
    client_id = await state.get_data()
    client_id = client_id.get('client_id')
    try:
        await  bot.send_message(chat_id=client_id, text=message.text)
    except:
        pass
    await state.reset_state()
    await state.reset_data()


@dp.callback_query_handler(Adminbot_callback.filter(action="canceladminbot_keyboard"), state=AdminPost.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Murojat rad etildi.", reply_markup=glav)
