from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.default.menuKeyboard import glav
from loader import dp, bot
from states.personalData import PersonalData


# /form komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
@dp.message_handler(Command("admin"))
async def enter_test(message: types.Message):
    await message.answer("Siz Admin uchun xabar jo'natmoqdasiz, Agarda sizga bot qaysidir joyda habar yubormagan bo'lsa, yoki murojat yo'llagan taqdiringizda 3 ish kunida ham javob kelmasa to'liq mazmunda so'rovingizni yuboring.\nBiz muamoni tez fursatda hal qilamiz.\nIltimos Admin uchun so'rov yuborishda quyidagilarni to'diring.")
    await message.answer("<b>Iltimos to'liq ismingizni kiriting</b>")
    await PersonalData.fullName.set()


@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {"name": fullname}
    )

    await message.answer("Email manzil kiriting")

    # await PersonalData.email.set()
    await PersonalData.next()


@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text

    await state.update_data(
        {"email": email}
    )

    await message.answer("Telefon raqam kiriting")

    await PersonalData.next()


@dp.message_handler(state=PersonalData.phoneNum)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text
    await state.update_data(
        {"phone": phone}
    )

    await message.answer("Xabaringizni yozing")

    await PersonalData.next()

@dp.message_handler(state=PersonalData.mazmun)
async def answer_phone(message: types.Message, state: FSMContext):
    mazmun = message.text
    await state.update_data(
        {"mazmun": mazmun}
    )

    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    mazmun = data.get("mazmun")

    msg = "Quyidai ma`lumotlar qabul qilindi:\n"
    msg += f"Ismingiz - {name}\n"
    msg += f"Email - {email}\n"
    msg += f"Telefon: - {phone}\n"
    msg += f"Xabar mazmuni: - {mazmun}"
    await message.answer(msg)




    # State dan chiqaramiz
    # 1-variant
    await state.finish()
    await message.answer("Siz bilan tez fursatda bog'lanamiz", reply_markup=glav)
    await bot.send_message(chat_id=1256224042, text=f"<b>Hurmatli Admin siz uchun habar bor\n {msg} </b>")
    # 2-variantl
    # await state.reset_state()

    # 3-variant. Ma`lumotlarni saqlab qolgan holda
    # await state.reset_state(with_data=False)
