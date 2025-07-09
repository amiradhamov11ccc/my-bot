from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import asyncio

TOKEN = "7754734695:AAEjg7HEXSPmNTE5JHgmt6JpXuGzr2uFqBU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Boshlang'ich 2 tugma
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb_builder = ReplyKeyboardBuilder()
    kb_builder.row(
        KeyboardButton(text="Ish izlayman"),
        KeyboardButton(text="Ish beraman")
    )
    keyboard = kb_builder.as_markup(resize_keyboard=True)
    await message.answer("Assalomu alaykum! Quyidagi tugmalardan birini tanlang:", reply_markup=keyboard)

VILOYATLAR = [
    "Toshkent", "Samarqand", "Buxoro", "Farg‘ona",
    "Namangan", "Andijon", "Qashqadaryo", "Surxondaryo",
    "Navoiy", "Xorazm", "Jizzax", "Sirdaryo"
]

KASBLAR = [
    "Dasturchi", "Muhandis", "Ustaxonachi", "Shifokor",
    "O‘qituvchi", "Sotuvchi"
]

def viloyat_keyboard():
    kb_builder = ReplyKeyboardBuilder()
    for i in range(0, len(VILOYATLAR), 3):
        kb_builder.row(*(KeyboardButton(text=v) for v in VILOYATLAR[i:i+3]))
    kb_builder.row(KeyboardButton(text="Orqaga"))
    return kb_builder.as_markup(resize_keyboard=True)

def kasb_keyboard():
    kb_builder = ReplyKeyboardBuilder()
    for i in range(0, len(KASBLAR), 3):
        kb_builder.row(*(KeyboardButton(text=k) for k in KASBLAR[i:i+3]))
    kb_builder.row(KeyboardButton(text="Orqaga"))
    return kb_builder.as_markup(resize_keyboard=True)

@dp.message()
async def handle_message(message: types.Message):
    text = message.text

    if text in ["Ish izlayman", "Ish beraman"]:
        await message.answer("Viloyatingizni tanlang:", reply_markup=viloyat_keyboard())

    elif text in VILOYATLAR:
        await message.answer(f"{text} viloyatini tanladingiz. Kasbingizni tanlang:", reply_markup=kasb_keyboard())

    elif text in KASBLAR:
        await message.answer(f"Siz {text} kasbini tanladingiz. Yaxshi tanlov!")

    elif text == "Orqaga":
        # Orqaga bosilganda bosh menyuga qaytamiz
        await cmd_start(message)

    else:
        await message.answer("Iltimos, menyudan tanlang!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
