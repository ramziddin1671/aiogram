from aiogram.types import CallbackQuery
import logging

from keyboards.inline.locationVaksina import backvaksina
from loader import dp, bot
from states.newpost import NewPost


@dp.callback_query_handler(text_contains="АДЪЮВАНТ")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://toshvziti.uz/media/images/1.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Vaktsinalar ishlab chiqarilishida qoʼllaniladigan “АДЪЮВАНТ” mahsuloti. АДЪЮВАНТ vaktsinalar ishlab chiqarishda, shu jumladan COVID-19 infektsiyasiga qarshi vaktsinalarda xam qoʼllanilib kelayotgan Аlyumin gidrooksidi oʼrninibosuvchi yoki uning turli kontsentratsiyasidagi maxsulot boʼlib, vaktsinalarning immunogenlik darajasini 10 marotabagacha oshirish imkonini beradi. Xomashyo: limfoid toʼqimasi mahsuloti va uning Аlyumin gidrooksidi bilan turli kontsentratsiyadagi eritmalari.</b>\nBog'lanish:  +998 94 924-33-88   +998 90 172-70-10 ",reply_markup=backvaksina)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="Бифидумбактерин")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://toshvziti.uz/media/images/images.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>«Бифидумбактерин» liofil quritish usulida hosil boʼladigan tirik 'Бифидумбактерин' dagi antagonistik faol xujayralarning quruq mikrob koʼrinishidagi biologik faol qoʼshimchasi. 'Бифидумбактерин' yosh bolalar va kattalardagi turli etiologiyasidagi disbakteriozni davolash va oldini olish uchun ishlatiladi. Goʼdaklarni ilk kunlaridan (shuningdek chala tugʼilgan) boshlab qoʼllash xam mumkin</b>\nBog'lanish:  +998 94 924-33-88   +998 90 172-70-10 ",reply_markup=backvaksina)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="Кальций Д3")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://toshvziti.uz/media/images/3.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b> “Кальций Д3” chaynaladigan tabletka shaklidagi biologik faol qoʼshimchasi organizm (suyaklarda, tishlarda, mushaklarda, tirnoqlarda, sochlarda)da kaltsiy va rux yetishmovchiligini samarali toʼldirib, osteoporoz va raxitni oldini oladi va qon tiklanishiga ijobiy taʼsir koʼrsatadi.</b>\nBog'lanish:  +998 94 924-33-88   +998 90 172-70-10 ",reply_markup=backvaksina)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="КОВИГЛОБИН")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://toshvziti.uz/media/images/4.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>Koviglobin preparati - Kovid-19 dan tuzalgan rekonvalesentlarning qon plazmasidan ajratib tozalangan va konsentrlangan gamma-globulin fraktsiyasi. Preparat tarkibida SARS-CoV2 koronavirus oqsillariga qarshi specifik antitanalar saqlaydi. Konservant va qo'shimcha yordam sifatida balqam kochiruvchi natriy benzoat preparatga 1 mg/ml dozada kiritiladi. Preparat shaffof, sarg'ish rangli, tiniq sargish suyuqlik va ampulalarda yoki flakonlarda 2 dan 10 ml gacha qadoqlanadi.</b>\nBog'lanish:  +998 94 924-33-88   +998 90 172-70-10 ",reply_markup=backvaksina)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="Ифаст")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://toshvziti.uz/media/images/5.png"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b> “Ифаст” inʼektsion shakldagi immunomodulyatori. “Ифаст” 1-24 soat ichida taʼsirini namoyon etadi (mavjudlari 7-14 kunda). Xomashyo: yirik shoxli hayvon limfoid toʼqimasi mahsulotlarining koʼp bosqichli qayta ishlash mahsuli.</b>\nBog'lanish:  +998 94 924-33-88   +998 90 172-70-10 ",reply_markup=backvaksina)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="МАГНИЙ В6")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    url_photo = "https://toshvziti.uz/media/images/vaksina_9AjJllx.jpg"
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer_photo(url_photo, caption="<b>«МАГНИЙ В6» kombinatsiyalashgan kompleks preparat boʼlib, bio magniy tuzlari va vitamin B6 dan iborat boʼlib, xujayraviy immunitetni qoʼllaydi, moddalar almashuvida ishtirok etadi, magniyni organizmda toʼgʼri taqsimlanishiga koʼmak berib, stress va nevrozlarda tinchlantiradi.</b>\nBog'lanish:  +998 94 924-33-88   +998 90 172-70-10 ",reply_markup=backvaksina)
    await call.answer(cache_time=60)