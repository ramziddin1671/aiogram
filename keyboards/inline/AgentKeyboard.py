from keyboards.inline.callback_data import boss_callback, xudud_callback, kamitet_callback
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1-usul.



categoryAgent = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📈 Agentlik haqida", callback_data="agent"),
            InlineKeyboardButton(text="💼 Rahbariyat", callback_data="boss"),
        ],
        [
            InlineKeyboardButton(text="📡 Hududiy bo'linmalar", callback_data="agentxudud"),
            InlineKeyboardButton(text="💳 Referent narxlar", callback_data="referentagent"),
        ],
        [
            InlineKeyboardButton(text="📊 Infografika", callback_data="infoagent"),
            InlineKeyboardButton(text="🛡 Litsenziyalash", callback_data="litsenziyaagent"),
        ],
        [
            InlineKeyboardButton(text="📍 Joylashuv", callback_data="locationAgent"),
        ],
        [
            InlineKeyboardButton(text="🔖 Korrupsion holat bo‘yicha murojaat yuborish", callback_data="searchagent"),
        ],
        [
            InlineKeyboardButton(text="🔗 Veb-saytga o'tish", url="https://uzpharmagency.uz/"),
            InlineKeyboardButton(text="🔍 Qidirish", switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="✉️ Botni ulashish", switch_inline_query="O‘zbekiston Respublikasi Sog‘liqni saqlash vazirligi huzuridagi Farmatsevtika tarmog‘ini rivojlantirish agentligi rasmiy telegram boti"),
        ],
    ])


# 2-usul raxbarlar qo'shamiz
coursesMenu = InlineKeyboardMarkup(row_width=1)

bossKariev = InlineKeyboardButton(text="Kariev Sardor Xikmatovich - Direktor", callback_data=boss_callback.new(item_name="bossKarievaa"))
coursesMenu.insert(bossKariev)

bossAkbarov = InlineKeyboardButton(text="Egamov Ulug‘bek Abduvaliyevich - Birinchi o‘rinbosar", callback_data=boss_callback.new(item_name="bossAkbarov"))
coursesMenu.insert(bossAkbarov)

bossEshmurodov = InlineKeyboardButton(text="Eshmuradov Jamshid Sheraliyevich - o'rinbosar", callback_data="boss:bossEshmuradov")
coursesMenu.insert(bossEshmurodov)

bossTemirov = InlineKeyboardButton(text="Temirov Baxodirxo'ja Baxromjon o'g'li - o'rinbosar", callback_data="boss:bossTemirov")
coursesMenu.insert(bossTemirov)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelAgent")
coursesMenu.insert(back_button)


back_buttonkamitet = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancelKamitet")



# 3 - usul xududiy raxbarlar qo'shamiz

books = {
    "Mansirov Ro’zimatali Siddikovich - Andijon": "xududMansirov",
    "Xudayev Vohidjon Shoyikulovich - Buxoro": "xududXudayev",
    "Xalxo’jayev Alijan Miyassarovich - Jizzax": "xuddudXalxo'jaev",
    "Aliev Umar Kuvatovich - Navoi": "xududAliev",
    "Umarov Ulug’bek Sobitxonovich - Namangan": "xududUmarov",
    "Qayumova Oydin Nematovna - Samarqand": "xududQayumova",
    "To’rayev Rasul Rustamovich - Sirdaryo": "xududTo’rayev",
    "Amonov Sherzod Ilhomovich - Surxondaryo": "xududAmonov",
    "Omilov Saxob Obidovich - Toshkent vil.": "xududOmilov",
    "Jumaniyozov Ulug’bek Botirovich - Toshkent": "xududJumaniyozov",
    "Fozilov Orifjon Murodilovich - Farg'ona": "xududFargona",
    "Jumaniyozov Osqarbek Sharipboyevich - Xorazm": "xududXorazm",
    "Xolmatov Saidqul Allamuratovich - Qashqadaryo": "xududXolmatov",
    "Serjanov Alisher Xalmuratovich - Qoraqalpogʼiston": "xududSerjanov",

}

xududMenu = InlineKeyboardMarkup(row_width=1)
for key, value in books.items():
    xududMenu.insert(InlineKeyboardButton(text=key, callback_data=xudud_callback.new(item_name=value)))
xududMenu.insert(back_button)



# farmkamitet uchun munu


categoryKamitet = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📈 'FMXM' DM haqida", callback_data="kamitet"),
            InlineKeyboardButton(text="💼 Rahbariyat", callback_data="bossKamitet"),
        ],
        [
            InlineKeyboardButton(text="📡 Bo'linmalar", callback_data="xududkamitet"),
            InlineKeyboardButton(text="📂 Reestr", callback_data="resterkamitet"),
        ],
        [
            InlineKeyboardButton(text="🖨 Nashrlar", callback_data="nashrkamitet"),
            InlineKeyboardButton(text="📝 Ko'p berilgan savollar", url="https://uzpharm-control.uz/"),
        ],
        [
            InlineKeyboardButton(text="📌 Farmakonazorat", callback_data="FarmakonazoratKamitet"),
            InlineKeyboardButton(text="📍 Joylashuv", callback_data="locationKamitet"),
        ],
        [
            InlineKeyboardButton(text="🔖 Korrupsion holat bo‘yicha murojaat yuborish", callback_data="searchkamitet"),
        ],
        [
            InlineKeyboardButton(text="🔗 Veb-saytga o'tish", url="https://uzpharm-control.uz/"),
            InlineKeyboardButton(text="🔍 Qidirish", switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="✉ ️Botni ulashish", switch_inline_query="O‘zbekiston Respublikasi Sog‘liqni saqlash vazirligi huzuridagi 'FARMATSEVTIKA MAHSULOTLARI XAVFSIZLIGI MARKAZI' DAVLAT MUASSASASI rasmiy telegram boti"),
        ],
    ])



bossKamitet = {
    "Direktor": "kamitetKariev",
    "Iqtisodiyot va moliya ishlari boʼyicha direktor oʼrinbosari": "kamitetInoyatov",
    "Farmatsevtika mahsulotlari xavfsizligi bo'yicha direktor oʼrinbosari": "kamitetTemirov",

}

bosskamitet = InlineKeyboardMarkup(row_width=1)
for key, value in bossKamitet.items():
    bosskamitet.insert(InlineKeyboardButton(text=key, callback_data=kamitet_callback.new(item_name=value)))
bosskamitet.insert(back_buttonkamitet)