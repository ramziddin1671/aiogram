from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1-usul.



categoryXimiya = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📈 Universitet xaqida", callback_data="UnXimiya"),
            InlineKeyboardButton(text="💼 Raxbariyat", callback_data="bossXimiya"),
        ],
        [
            InlineKeyboardButton(text="📋 Jurnal", callback_data="XimiyaJurnal"),
            InlineKeyboardButton(text="📖 Ilmiy Kengash", callback_data="XimiyaKengash"),
        ],
        [
            InlineKeyboardButton(text="💊 Maxsulotlar", callback_data="XimiyaProduct"),
            InlineKeyboardButton(text="🙋‍♂️ Ko'p beriladigan savollar", url="https://uzpharmagency.uz/"),
        ],
        [
            InlineKeyboardButton(text="📍 Location", callback_data="locationXimiya"),
        ],
        [
            InlineKeyboardButton(text="🔖 Adminga So'rov qoldirish", callback_data="searchagent"),
        ],
        [
            InlineKeyboardButton(text="🔗 Veb saytga o'tish", url="https://uzpharmagency.uz/"),
            InlineKeyboardButton(text="🔍 Qidirish", switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="✉️Botni Ulashish", switch_inline_query="O‘zbekiston Respublikasi Sog‘liqni saqlash vazirligi huzuridagi Farmatsevtika tarmog‘ini rivojlantirish agentligi rasmiy telegram boti"),
        ],
    ])