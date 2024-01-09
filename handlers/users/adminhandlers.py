import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentTypes
from data.config import ADMINS
from filters import IsPrivate
from keyboards.default.menuKeyboard import glav
from keyboards.default.startKeyboard import CancelAdminBtn
from keyboards.inline.murojatKamitetlar import NewAdmin
from loader import dp, db, bot
from states.newpost import AdminStates


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    unactive = 0
    for user in users:
        try:
            # print(user[3])
            user_id = user[3]
            await bot.send_message(chat_id=user_id, text="Референт нарх шакллантириш тизими доирасида дори воситаларига чекланган нархларни қайд этиш қандай амалга оширилади? Ушбу қўлланмада мазкур тартиб ҳақида батафсил маълумотга эга бўласиз. <a href='https://uzpharm-control.uz/ru/registries/api-mpip'><b>Қўланмани кўриш</b></a>")
            await asyncio.sleep(0.05)
        except Exception as ex:
            # await bot.send_message(chat_id=ADMINS[0], text=f'Log: {ex}')
            unactive += 1
    await bot.send_message(chat_id=ADMINS[0], text=f"unactivlar soni: {unactive} ")


@dp.message_handler(text='❌ Bekon qilish (admin)', state='*')
async def cancel_btn(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(text='Admin panel', reply_markup=glav)


@dp.message_handler(text="/reklamaa",user_id=ADMINS)
async def send_post(message: Message):
    await message.answer(text='Tayyor xabaringizni yuboring:', reply_markup=CancelAdminBtn)
    await AdminStates.Post.set()


@dp.message_handler(state=AdminStates.Post, content_types=ContentTypes.ANY)
async def user_post(message: Message, state: FSMContext):
    await message.answer(text="Ushbu xabar barcha foydalanuvchilarga borsinmi?")
    await bot.copy_message(
        chat_id = message.from_user.id,
        from_chat_id = message.from_user.id,
        message_id = message.message_id,
        reply_markup = await NewAdmin(user_id=message.from_user.id)
    )
    await state.update_data({'message_id': message.message_id})


@dp.callback_query_handler(text_contains='new_admin', state=AdminStates.Post)
async def send_message(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    msg_id = await state.get_data()
    data = call.data.rsplit(':')
    # new_admin:accept:2641316
    if data[1] == 'accept':
        unactive = 0
        for user in await db.select_all_users():
            try:
                await bot.copy_message(
                    chat_id = user[3],
                    from_chat_id = call.from_user.id,
                    message_id = msg_id.get('message_id')
                )
            except:
                unactive += 1
        await call.message.answer(text=f"✅ Xabar barcha aktiv foydalanuvchilarga yuborildi \nunactivlar soni - {unactive}",
                              reply_markup=glav)
    else:
        await call.message.answer(text='❌ Bekor qilindi', reply_markup=glav)
    await state.reset_state()



@dp.message_handler(text="/vakant", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    unactive = 0
    for user in users:
        try:
            # print(user[3])
            user_id = user[3]
            await bot.send_message(chat_id=user_id, text="Hurmatli foydalanuvchilar diqqatiga"
                                                         " DORI VOSITALARI, TIBBIY BUYUMLAR VA TIBBIY TEXNIKA EKSPERTIZASI VA STANDARTLASHTIRISH DAVLAT MARKAZI "
                                                         "<a href='https://uzpharm-control.uz/uz/vacancies'> rasmiy veb-sahifasida</a> ishga kirish uchun ochiq tanlov e'lon qilindi."
                                                         "\nTanlovda ishtirok tish muddati 05.12.2022-15-12-2022")
            await asyncio.sleep(0.05)
        except Exception as ex:
            # await bot.send_message(chat_id=ADMINS[0], text=f'Log: {ex}')
            unactive += 1
    await bot.send_message(chat_id=ADMINS[0], text=f"unactivlar soni: {unactive} ")

@dp.message_handler(text="/yacheyka", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    unactive = 0
    for user in users:
        try:
            # print(user[3])
            user_id = user[3]
            await bot.send_message(chat_id=user_id, text="Hurmatli foydalanuvchilar diqqatiga\nDORI VOSITALARI, TIBBIY BUYUMLAR VA TIBBIY TEXNIKA EKSPERTIZASI VA STANDARTLASHTIRISH DAVLAT MARKAZIGA, ishga kirish uchun ochiq tanlovda qatnashgan barcha foydalanuvchilar kommisiya a'zolari tomonidan o'rganilib chiqilib, foydalanuvchilarning yacheykalariga ma'lumotlar yuborilganini ma'lum qilamiz !")
            await asyncio.sleep(0.05)
        except Exception as ex:
            # await bot.send_message(chat_id=ADMINS[0], text=f'Log: {ex}')
            unactive += 1
    await bot.send_message(chat_id=ADMINS[0], text=f"unactivlar soni: {unactive} ")
#nigadir ishlamayapti google

@dp.message_handler(commands='change_photo', is_chat_admin=True)
async def chat_admin_example(msg: types.Message):
    await msg.answer(f"rasmni o'zgartiramizmi")


@dp.message_handler(IsPrivate(), is_chat_admin=True)
async def chat_admin_example(msg: types.Message):
    await msg.answer(f"Nima xizmat")




