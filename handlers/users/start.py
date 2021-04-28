from aiogram import types
from loader import dp


def get_keyboard():
    buttons = [
        types.InlineKeyboardButton(text="Русский", callback_data="language.1"),
        types.InlineKeyboardButton(text="English", callback_data="language.2"),
        types.InlineKeyboardButton(text="Український", callback_data="language.3"),
        types.InlineKeyboardButton(text="Español", callback_data="language.4"),
        types.InlineKeyboardButton(text="Português", callback_data="language.5"),
        types.InlineKeyboardButton(text="adg", callback_data="language.6"),
        types.InlineKeyboardButton(text="sfdsgg", callback_data="language.7"),
        types.InlineKeyboardButton(text="sadasd", callback_data="language.8"),
        types.InlineKeyboardButton(text="ukghj", callback_data="language.9"),
        types.InlineKeyboardButton(text="uuyh", callback_data="language.10"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    await message.answer("<b>Выберите язык:</b>", reply_markup=get_keyboard())

@dp.callback_query_handler(text_contains="language.")
async def language(call: types.CallbackQuery):

    await call.message.answer("ТЫ пидор")