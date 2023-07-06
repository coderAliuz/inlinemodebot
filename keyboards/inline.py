from aiogram.types.inline_keyboard import InlineKeyboardButton,InlineKeyboardMarkup

pyhton_inline_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Kursga yozilish",url="https://t.me//coder_ali"),
         InlineKeyboardButton(text="Kurs haqida",callback_data="python")]
    ]
)

check_info_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="ha",callback_data="yes"),
        InlineKeyboardButton(text="yo'q",callback_data="no"),
         ]
    ]
)