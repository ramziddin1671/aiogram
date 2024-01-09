from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp


@dp.message_handler(Text(startswith='qale',ignore_case=True))
@dp.message_handler(Text(contains=['assalom', 'salom'],ignore_case=True))
@dp.message_handler(Text(equals='Assalomu alylum', ignore_case=True))
async def text_example(msg: types.Message):
    await msg.reply(f"Vaaleykum assalom")


# Boshqa parametrlar
#startswith
#endswith