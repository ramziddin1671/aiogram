from aiogram import types
from aiogram.dispatcher.filters import Regexp
from loader import dp

# i hate regex sayitidan danilar olindi
EMAIL_REGETX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHON_NUMBER = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
COMMAND_EMAIL_REGETX = r'/email:' + EMAIL_REGETX

@dp.message_handler(Regexp(EMAIL_REGETX))
async def regexp_email(msg: types.Message):
    await msg.answer(f"Email qabul qilindi")


@dp.message_handler(Regexp(PHON_NUMBER))
async def phon_regexp(msg: types.Message):
    await msg.answer(f"Telefon nomer qabul qilindi")


@dp.message_handler(regexp_commands=[COMMAND_EMAIL_REGETX])
async def command_regexp_email(msg: types.Message):
    await msg.answer(f"Email qabul qilindi")
