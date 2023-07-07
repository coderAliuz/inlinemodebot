from aiogram.types import Message
from config import dp ,bot,admin
from state import AdminState
from model import get_chat_ids,count_users
from keyboards import admin_kb,back_kb

@dp.message_handler(chat_id=admin,commands="start",state="*")
async def admin_start(message:Message):
    await message.answer("Salom admin.\nKerakli tugmani bos",reply_markup=admin_kb)
    await AdminState.main.set()

@dp.message_handler(text="Bot haqida",state=AdminState.main)
async def about_bot(message:Message):
    info=count_users()
    await message.reply(f"Bot foydalanuvchilari -{info} ta")

@dp.message_handler(text="Xabar yuborish",state=AdminState.main)
async def send_mess(message:Message):
    await message.answer("Istalgan xabar yuboring. Bu xabar barcha foydalanuvchilarga yuboriladi",reply_markup=back_kb)
    await AdminState.next()

@dp.message_handler(content_types="text",state=AdminState.message)
async def send_text(message:Message):
    text=message.text
    if text=="Ortga":
        await message.answer("Kerakli tugamini bosing",reply_markup=admin_kb)
        await AdminState.previous()
    else:
        for i in get_chat_ids():
            try:
                await bot.send_message(i[0],text)
            except:pass
        await message.answer("Xabar yuborildi")

