from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


AdminKamitet = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔖 So'rov qoldirish", callback_data="murojatKamitet"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backKamitet"),
        ],
    ])



MurojatKamitet = InlineKeyboardMarkup(
    inline_keyboard=[
        # [
        #     InlineKeyboardButton(text="🔖 So'rov qoldirish", callback_data="murojatKamKariev"),
        # ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backKamKariev"),
        ],
    ])

murojatSaidov = InlineKeyboardMarkup(
    inline_keyboard=[
        # [
        #     InlineKeyboardButton(text="🔖 So'rov qoldirish", callback_data="testmurojatKamitet"),
        # ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="testbackKamitet"),
        ],
    ])

murojatInayatov = InlineKeyboardMarkup(
    inline_keyboard=[
        # [
        #     InlineKeyboardButton(text="🔖 So'rov qoldirish", callback_data="murojatKamitetinayatov"),
        # ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backKamitetinayatov"),
        ],
    ])

murojatAzizov = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔖 So'rov qoldirish", callback_data="murojatKamitetazizov"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backKamitetazizov"),
        ],
    ])

murojatMusaev = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔖 So'rov qoldirish", callback_data="murojatKamitetmusaev"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backKamitetmusaev"),
        ],
    ])

murojatXasanov = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔖 So'rov qoldirish", callback_data="murojatKamitetxasanov"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backKamitetxasanov"),
        ],
    ])

murojatAchilov = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔖 So'rov qoldirish", callback_data="murojatKamitetachilov"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backKamitetachilov"),
        ],
    ])

murojatBoltaboeva = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔖 So'rov qoldirish", callback_data="murojatKamitetboltaboeva"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backKamitetboltaboeva"),
        ],
    ])

murojatSalieva = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔖 So'rov qoldirish", callback_data="murojatKamitetsalieva"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backKamitetsalieva"),
        ],
    ])

murojatAbduraxmonov = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔖 So'rov qoldirish", callback_data="murojatKamitetAbduraxmonov"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="backKamitetAbduraxmonov"),
        ],
    ])


async def NewAdmin(user_id: int):
    btn = InlineKeyboardMarkup(row_width=1)
    btn.insert(InlineKeyboardButton(text='✅ Tasdiqlash', callback_data=f'new_admin:accept:{user_id}'))
    btn.insert(InlineKeyboardButton(text='❌ Rad etish', callback_data=f'new_admin:reject:{user_id}'))
    return btn