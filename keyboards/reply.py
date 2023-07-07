from aiogram.types.reply_keyboard import ReplyKeyboardMarkup,ReplyKeyboardRemove

main_kb=ReplyKeyboardMarkup(
    [
        ["Men haqimda"],
        ["Tahrirlash","O'chirish"],
        ["Bot haqida"]
    ],resize_keyboard=True
)
back_kb=ReplyKeyboardMarkup(
    [
        ["Ortga"]
    ],resize_keyboard=True
)

edit_kb=ReplyKeyboardMarkup(
    [
        ["Ism va Familiya","Telefon raqam"],
        ["Ortga"]
    ],resize_keyboard=True
)

admin_kb=ReplyKeyboardMarkup(
    [
        ["Xabar yuborish","Bot haqida"]
    ],resize_keyboard=True
)
del_kb=ReplyKeyboardRemove()