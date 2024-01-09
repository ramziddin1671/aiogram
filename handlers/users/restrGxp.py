from keyboards.inline.locationKamitet import backGxp, backbackGxp
from loader import dp, bot
from states.newpost import AgentAdmin, AdminGxp
import logging
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, contact


@dp.callback_query_handler(text_contains="GMP")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.delete()
    text = f"GMP reestri bo'yicha\n"
    text += f"To'liq mazmunda tanishib chiqish uchun: <a href='https://uzpharm-gxp.uz/oz/registry2'>Batavsil</a>  \n"
    await call.answer(cache_time=60)
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text, reply_markup=backbackGxp)


@dp.callback_query_handler(text_contains="GDP")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    await call.message.delete()
    text = f"GDP reestri bo'yicha\n"
    text += f"To'liq mazmunda tanishib chiqish uchun: <a href='https://uzpharm-gxp.uz/oz/registry3'>Batavsil</a>   \n"
    await call.answer(cache_time=60)
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text, reply_markup=backbackGxp)