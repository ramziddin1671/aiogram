from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


MurojatKarievAgent = InlineKeyboardMarkup(
    inline_keyboard=[
        # [
        #     InlineKeyboardButton(text="🔖 So'rov qoldirish", callback_data="murojatKariev"),
        # ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backKariev"),
        ],
    ])

MurojatAkbarovAgent = InlineKeyboardMarkup(
    inline_keyboard=[
        # [
        #     InlineKeyboardButton(text="🔖 So'rov qoldirish", callback_data="murojatAkbarov"),
        # ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backAkbarov"),
        ],
    ])

MurojatTemirovAgent = InlineKeyboardMarkup(
    inline_keyboard=[
        # [
        #     InlineKeyboardButton(text="🔖 So'rov qoldirish", callback_data="murojatTemirov"),
        # ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backTemirov"),
        ],
    ])

MurojatBegmatovaAgent = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔖 So'rov qoldirish", callback_data="murojatBegmatova"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backBegmatova"),
        ],
    ])