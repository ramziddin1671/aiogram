from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.message_handler(commands='xarid')
async def set_state(msg: types.Message, state: FSMContext):
    """Foydalanuvchini state muxitiga otqazamiz"""
    await state.set_state('xarid_state')
    await msg.answer(f"Maxsulot tanlang")


@dp.message_handler(state='xarid_state')
async def state_example(msg: types.Message, state: FSMContext):
    await msg.answer(f"Maxsulot savatga qo'shildi")
    await state.finish()
