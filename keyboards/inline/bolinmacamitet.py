from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.AgentKeyboard import back_buttonkamitet
from keyboards.inline.callback_data import bolinmacamitet_callback

bolinmaKamitet = {
    "Dori vositalari sifatini nazorat qilish va standartlashtirish laboratoriyasi": "kamitetlaboratory",
    "Farmako-toksikologik tadqiqot laboratoriyasi": "kamitettaksikolog",
    "Farmakopeya qoʻmitasi": "kamitetfarmakopea",
    "Farmokologiya Komiteti": "kamitetfarmakalogiya",
    "Narkotik moddalarni nazorat qilish qoʻmitasi": "kamitetnarkotik",
    "Poligrafiya bo'limi": "kamitetpoligrafiya",
    "Qiyoslash laboratoriyasi": "kamitetqiyoslash",
    "Ro'yxatga olish bo'limi": "kamitetRoyxat",
    "Tibbiy buyumlar va tibbiy texnika sifatini nazorat qilish laboratoriyasi": "kamitetsifatnazorat",
    "Vaksinalar, sarum preparatlari va mikrobiologik tadqiqotlar laboratoriyasi": "kamitetvaksina",
    "Yangi tibbiy texnika qo'mitasi": "kamitetyangitexnika",
    "Zarur amaliyotlar (GxP) milliy inspektorati boʻlimi": "kamitetGxP",

}

bolinmaKamitets = InlineKeyboardMarkup(row_width=1)
for key, value in bolinmaKamitet.items():
    bolinmaKamitets.insert(InlineKeyboardButton(text=key, callback_data=bolinmacamitet_callback.new(item_name=value)))
bolinmaKamitets.insert(back_buttonkamitet)


