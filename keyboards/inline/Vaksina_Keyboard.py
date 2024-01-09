from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1-usul.
from keyboards.inline.callback_data import vaksina_callback, productvak_callback, kengashvak_callback
from keyboards.inline.locationVaksina import backvaksina

categoryVaksina = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📈 Universitet haqida", callback_data="UnVaksina"),
            InlineKeyboardButton(text="💼 Rahbariyat", callback_data="bossVaksina"),
        ],
        [
            InlineKeyboardButton(text="💊 Mahsulotlar", callback_data="VaksinaProduct"),
            InlineKeyboardButton(text="📖 Ilmiy Kengash", callback_data="VaksinaKengash"),
        ],
        [
            InlineKeyboardButton(text="📍 Joylashuv", callback_data="locationVaksina"),
        ],
        [
            InlineKeyboardButton(text="🔖 Korrupsion holat bo‘yicha murojaat yuborish", callback_data="searchvak"),
        ],
        [
            InlineKeyboardButton(text="🔗 Veb-saytga o'tish", url="https://toshvziti.uz/ru/"),
            InlineKeyboardButton(text="🔍 Qidirish", switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="✉ ️Botni ulashish", switch_inline_query="O‘zbekiston Respublikasi Sog‘liqni saqlash vazirligi huzuridagi Farmatsevtika tarmog‘ini rivojlantirish agentligi rasmiy telegram boti"),
        ],
    ])


vaksinaRaxbar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Direktor", callback_data="vaksinaAshurov"),

        ],
        [
            InlineKeyboardButton(text="Institut direktorining ilmiy ishlar boʼyicha oʼrinbosari", callback_data="vaksinaMamatqulov"),
        ],
        [
            InlineKeyboardButton(text="Ilmiy kotib", callback_data="vaksinaMaxmudjonova"),
        ],
        [
            InlineKeyboardButton(text="Institut direktorining umumiy ishlar boʼyicha oʼrinbosari",
                                 callback_data="vaksinaDadajonov"),
        ],
        [
            InlineKeyboardButton(text="Bosh hisobchi", callback_data="kamitetAssadulaev"),
        ],
        [
            InlineKeyboardButton(text="ortga", callback_data="cancelvaksina"),
        ],
        ])


productvaksina = {
    "АДЪЮВАНТ": "АДЪЮВАНТ",
    "Бифидумбактерин": "Бифидумбактерин",
    "Кальций Д3": "Кальций Д3",
    "KOVIGLOBIN": "КОВИГЛОБИН",
    "Ифаст": "Ифаст",
    "МАГНИЙ В6": "МАГНИЙ В6",
    "Ortga": "cancelvaksina",

}

product_Vak = InlineKeyboardMarkup(row_width=1)
for key, value in productvaksina.items():
    product_Vak.insert(InlineKeyboardButton(text=key, callback_data=productvak_callback.new(item_name=value)))


kengashvaksina = {
    "Aprobatsiya bo'yicha seminar kengashi": "kengash1",
    "ixtisoslashgan kengash": "kengash2",
    "Ortga": "cancelvaksina",

}

kengash_Vak = InlineKeyboardMarkup(row_width=1)
for key, value in kengashvaksina.items():
    kengash_Vak.insert(InlineKeyboardButton(text=key, callback_data=kengashvak_callback.new(item_name=value)))
