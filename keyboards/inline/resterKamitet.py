from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



ResterKamitet = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Dori vositalari va tibbiy buyumlarning davlat reestri.", callback_data="resterDori"),
        ],
        [
            InlineKeyboardButton(text="Yaroqsiz deb topilgan tibbiy mahsulotlar boʻyicha maʼlumot", callback_data="resterYaroqsiz"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backrester"),
        ],
    ])



ResterDori = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tibbiy amaliyotida foydalanish uchun tasdiqlangan 2023-yil 27-sonli qo'shimchalar.", callback_data="rester05_11_21"),
        ],
        [
            InlineKeyboardButton(text="Tibbiyot amaliyotida foydalanishga ruxsat berilgan dori vositalari", callback_data="rester21_01_21"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backrester"),
        ],
    ])


ResterYaroqsiz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="2023 1-kv da yaroqsiz deb topilgan tibbiy mahsulotlar boʻyicha maʼlumot", callback_data="resteryaroqsiz1"),
        ],
        [
            InlineKeyboardButton(text="2023 2-kv da yaroqsiz deb topilgan tibbiy mahsulotlar boʻyicha maʼlumot",
                                 callback_data="resteryaroqsiz2"),
        ],
        [
            InlineKeyboardButton(text="2023 3-kv da yaroqsiz deb topilgan tibbiy mahsulotlar boʻyicha maʼlumot",
                                 callback_data="resteryaroqsiz3"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backrester"),
        ],
    ])