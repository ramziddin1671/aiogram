import logging
import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startKeyboard import menuStart
from keyboards.inline.AgentKeyboard import categoryKamitet
from states.personalData import PersonalData
from aiogram.dispatcher import FSMContext
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
from keyboards.default.menuKeyboard import menu
from filters.private_chat import IsPrivate


# deep_link bu qaysi saytdan kelgan foydalanuvchilarni nazorat qilish imkoni
@dp.message_handler(IsPrivate(), CommandStart(deep_link='kun.uz'))
async def bot_start(message: types.Message):
    args = message.get_args()
    text = f'Salom, {message.from_user.full_name}!\n'
    text += f"Sizni {args} tavsiya qildi"
    await message.answer(text)


# @dp.message_handler(commands='boshla') bu ikkinchi yo'li xoxlasang /boshla qilsa bo'ladi
@dp.message_handler(IsPrivate(),commands='start')
async def bot_start(message: types.Message):
    logging.info(f"{message.from_user.id=}") #user xaqida ma'lumotni konsulga chiqarish
    logging.info(f"{message.from_user.full_name=}")
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)
    text = f'Assalomu alaykum, hurmatli, {message.from_user.full_name}!\n'
    text += f"<b>Siz OʻZBEKISTON RESPUBLIKASI SOG'LIQNI SAQLASH VAZIRLIGI HUZURIDAGI 'FARMATSEVTIKA MAHSULOTLARI XAVFSIZLIGI MARKAZI' rasmiy botiga xush kelibsiz !</b>\n"
    text += f"siz markazimiz haqida maʼlumot olishingiz hamda korrupsiya holatlari boʻyicha murojaat yoʻllashingiz mumkin !\n☎ Telefon raqamlarimiz: \n📱 (71)203-01-01\n📱 242-69-58, 242-48-93\n📨 farmkomitet@ssv.uz\n🖥 Veb-sahifamiz:\n🌎 uzpharm-control.uz\n"
    await message.answer(text,  reply_markup=categoryKamitet)

    # ADMINGA xabar beramiz
    count = await db.count_users()
    msg = f"{message.from_user.username}, yoki {message.from_user.get_mention()}  {message.from_user.full_name},\n{message.from_user.id=}\n bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)
