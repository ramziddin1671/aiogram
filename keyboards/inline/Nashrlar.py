from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



NashrKamitet = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Farmasevtik xabarnomasi", callback_data="xabarnomanashr"),
        ],
        [
            InlineKeyboardButton(text="Davlat farmakopeyasi", callback_data="davlatnashr"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backnashr"),
        ],
    ])


NashrXabarnoma = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="	Oʻzbekiston farmasevtik xabarnomasi № 1-2/2023", callback_data="xabarnoma4"),
        ],
        [
            InlineKeyboardButton(text="	Oʻzbekiston farmasevtik xabarnomasi № 1-4/2022", callback_data="xabarnoma0"),
        ],
        [
            InlineKeyboardButton(text="	Oʻzbekiston farmasevtik xabarnomasi №1/2021", callback_data="xabarnoma1"),
        ],
        [
            InlineKeyboardButton(text="	Oʻzbekiston farmasevtik xabarnomasi №2/2021", callback_data="xabarnoma2"),
        ],
        [
            InlineKeyboardButton(text=" Oʻzbekiston farmasevtik xabarnomasi №3-4/2021", callback_data="xabarnoma3"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backnashr"),
        ],
    ])


NashrDavlat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbekiston Respublikasi Davlat farmokopeyasi 1 - nashr 2 - jildi bo'yicha umumlashtirilgan ma'lumot (2022)", callback_data="davlatnashr1"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backnashr"),
        ],
    ])