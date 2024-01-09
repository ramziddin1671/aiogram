from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
import logging
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, contact

from keyboards.default.menuKeyboard import menu, glav
from keyboards.inline.AgentKeyboard import categoryAgent
from keyboards.inline.locationAgent import backagent
from loader import dp, bot
from states.newpost import NewPost


@dp.callback_query_handler(text_contains="xududMansirov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/thumb/view/w/200/h/200/src/uploads/territorial/2fa98920c71667b249d6806f5a954d20.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Mansirov Ro’zimatali Siddikovich\n'Аndijon viloyati farmatsevtika tarmogʼini rivojlantirish bo’linmasi'</b>\nBog'lanish:  +998 94 924-33-88;  +998 90 172-70-10 ",reply_markup=backagent)
    await call.answer(cache_time=60)


#2chi raxbar
@dp.callback_query_handler(text_contains="xududXudayev")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/thumb/view/w/200/h/200/src/uploads/territorial/4767f74117626ec3601878f590bdc89f.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Xudayev Vohidjon Shoyikulovich\n'Buxoro viloyati farmatsevtika tarmogʼini rivojlantirish bo’linmasi'</b>\nBog'lanish: +998 93 625-03-70", reply_markup=backagent)
    await call.answer(cache_time=60)


#3chi raxbar
@dp.callback_query_handler(text_contains="xuddudXalxo'jaev")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/thumb/view/w/200/h/200/src/uploads/territorial/ac83cbb64b819c834e77a1f0f7fac08b.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Xalxo’jayev Alijan Miyassarovich\n'Jizzax viloyati farmatsevtika tarmogʼini rivojlantirish bo’linmasi'</b>\nBog'lanish: +998 71 203-81-81; +998 97 784-11-81  ", reply_markup=backagent)
    await call.answer(cache_time=60)


#4chi raxbar
@dp.callback_query_handler(text_contains="xududAliev")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/thumb/view/w/200/h/200/src/uploads/territorial/ac8de299f92f71552eb9d7b570acd356.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Aliev Umar Kuvatovich\n'Navoiy viloyati farmatsevtika tarmogʼini rivojlantirish bo’linmasi'</b>\nBog'lanish: +998 97 297-65-77", reply_markup=backagent)
    await call.answer(cache_time=60)


#5chi raxbar
@dp.callback_query_handler(text_contains="xududUmarov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/thumb/view/w/200/h/200/src/uploads/territorial/6ab9bb67ad21e7a0400afb606bc6a9f5.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Umarov Ulug’bek Sobitxonovich\n'Namangan viloyati farmatsevtika tarmogʼini rivojlantirish bo’linmasi'</b>\nBog'lanish:+998 91 354-03-04; +998 94 274-68-61  ", reply_markup=backagent)
    await call.answer(cache_time=60)


#6chi raxbar
@dp.callback_query_handler(text_contains="xududQayumova")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/thumb/view/w/200/h/200/src/uploads/territorial/1b48367e120dab7022af638ce1ab9cac.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Qayumova Oydin Nematovna\n'Samarqand viloyati farmatsevtika tarmogʼini rivojlantirish bo’linmasi'</b>\nBog'lanish:+998 91 542-37-17; +998 99 311-37-17 ", reply_markup=backagent)
    await call.answer(cache_time=60)


#7chi raxbar
@dp.callback_query_handler(text_contains="xududTo’rayev")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/thumb/view/w/200/h/200/src/uploads/territorial/b07e0e105df14b2030cf513362006530.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>To’rayev Rasul Rustamovich\n'Sirdaryo viloyati farmatsevtika tarmogʼini rivojlantirish boshqarmasi'</b>\nBog'lanish:+998 97 278-12-22", reply_markup=backagent)
    await call.answer(cache_time=60)


#8chi raxbar
@dp.callback_query_handler(text_contains="xududAmonov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/thumb/view/w/200/h/200/src/uploads/territorial/6577e53b1036c1466bd2e4e5987a1bad.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Amonov Sherzod Ilhomovich\n'Surxondaryo viloyati farmatsevtika tarmogʼini rivojlantirish boshqarmasi'</b>\nBog'lanish: +998 97 778-09-80; +998 99 900-09-80 ", reply_markup=backagent)
    await call.answer(cache_time=60)


#9chi raxbar
@dp.callback_query_handler(text_contains="xududOmilov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/thumb/view/w/200/h/200/src/uploads/territorial/b3f75902121f670d9551814624ed47fc.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Omilov Saxob Obidovich\n'Toshkent viloyati farmatsevtika tarmogʼini rivojlantirish boshqarmasi'</b>\nBog'lanish: +998 71 203-81-81 ", reply_markup=backagent)
    await call.answer(cache_time=60)


#10chi raxbar
@dp.callback_query_handler(text_contains="xududJumaniyozov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/thumb/view/w/200/h/200/src/uploads/territorial/cfcb657e741740236ec9aaa9fcc4631c.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Jumaniyozov Ulug’bek Botirovich\n'Toshkent shahar farmatsevtika tarmogʼini rivojlantirish boshqarmasi'</b>\nBog'lanish: +998 71 203-81-81", reply_markup=backagent)
    await call.answer(cache_time=60)


#11chi raxbar
@dp.callback_query_handler(text_contains="xududFargona")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/uploads/territorial/ac86534d8ad948189ca17a9bb7a0d07e.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Fozilov Orifjon Murodilovich\n'Fargʼona viloyati farmatsevtika tarmogʼini rivojlantirish boshqarmasi'</b>\nBog'lanish:  +998 97 271-12-77", reply_markup=backagent)
    await call.answer(cache_time=60)


#12chi raxbar
@dp.callback_query_handler(text_contains="xududXorazm")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/thumb/view/w/200/h/200/src/uploads/territorial/00b05ecd4c634f6c199d71f97de1a75b.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Jumaniyozov Osqarbek Sharipboyevich\n'Xorazm viloyati farmatsevtika tarmogʼini rivojlantirish boshqarmasi'</b>\nBog'lanish:  +998 97 514 66 62; +998 93 753 06 28  ", reply_markup=backagent)
    await call.answer(cache_time=60)


#13chi raxbar
@dp.callback_query_handler(text_contains="xududXolmatov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/thumb/view/w/200/h/200/src/uploads/territorial/3df2a79fd1155510be0be1d74d8db827.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Xolmatov Saidqul Allamuratovich\n'Qashqadaryo viloyati farmatsevtika tarmogʼini rivojlantirish bo’linmasi'</b>\nBog'lanish:  +998 90-680-78-78", reply_markup=backagent)
    await call.answer(cache_time=60)


#14chi raxbar
@dp.callback_query_handler(text_contains="xududSerjanov")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://uzpharmagency.uz/thumb/view/w/200/h/200/src/uploads/territorial/2b8e950a9357584684c791137ffc7e20.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Serjanov Alisher Xalmuratovich\n'Qoraqalpogʼiston Respublikasi farmatsevtika tarmogʼini rivojlantirish bo’linmasi'</b>\nBog'lanish: +998 90 727-55-56", reply_markup=backagent)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="cancelAgent")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz
    await call.message.delete()
    await call.message.answer("Bo'limlardan birini tanlang: ", reply_markup=categoryAgent)