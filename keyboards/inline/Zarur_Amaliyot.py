from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1-usul.
from keyboards.inline.callback_data import boss_callback

categoryGxp = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📈 Markaz haqida", callback_data="Gxp"),
            InlineKeyboardButton(text="💼 Rahbariyat", callback_data="bossGxp"),
        ],
        [
            InlineKeyboardButton(text="📡 Bo'linmalar", callback_data="bolinmaGxp"),
            InlineKeyboardButton(text="📂 Reester", callback_data="RestrGxp"),
        ],
        [
            InlineKeyboardButton(text="📋 Tuzilma", callback_data="TuzulmaGxp"),
            InlineKeyboardButton(text="🙋‍♂️ Ko'p beriladigan savollar", url="https://uzpharm-gxp.uz/oz/faq"),
        ],
        [
            InlineKeyboardButton(text="📍 Joylashuv", callback_data="locationGxp"),
        ],
        [
            InlineKeyboardButton(text="🔖 Korrupsion holat bo‘yicha murojaat yuborish", callback_data="searchGxp"),
        ],
        [
            InlineKeyboardButton(text="🔗 Veb-saytga o'tish", url="https://uzpharm-gxp.uz/"),
            InlineKeyboardButton(text="🔍 Qidirish", switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="✉ ️Botni ulashish", switch_inline_query="O‘zbekiston Respublikasi Sog‘liqni saqlash vazirligi huzuridagi Farmatsevtika tarmog‘ini rivojlantirish agentligi rasmiy telegram boti"),
        ],
    ])


RaxbarGxp = InlineKeyboardMarkup(row_width=1)

bossKariev = InlineKeyboardButton(text="Dusmatov Aziz Fayzamatovich - Direktor", callback_data=boss_callback.new(item_name="bossDusmatov"))
RaxbarGxp.insert(bossKariev)

bossAkbarov = InlineKeyboardButton(text="Ibragimov Avazbek Baxtiyarovich - Direktor o'rinbosari", callback_data=boss_callback.new(item_name="bossIbragimov"))
RaxbarGxp.insert(bossAkbarov)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelGxp")
RaxbarGxp.insert(back_button)


RestrGxp = InlineKeyboardMarkup(row_width=1)

restrgmp = InlineKeyboardButton(text="GMP", callback_data=boss_callback.new(item_name="GMP"))
RestrGxp.insert(restrgmp)

restrgdp = InlineKeyboardButton(text="GDP", callback_data=boss_callback.new(item_name="GDP"))
RestrGxp.insert(restrgdp)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelGxp")
RestrGxp.insert(back_button)


