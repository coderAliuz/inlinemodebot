from aiogram.types import Message
from config import dp
from aiogram.dispatcher import FSMContext
from state import UserState

@dp.message_handler(commands="start",state="*")
async def start(message:Message,state: FSMContext):
    await message.answer("Salom xush kelibsiz\nIsm va Familiyani kiriting")
    await message.answer_photo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuPuTdklROISkl9QnpjBvvpO9f34rpJfBLRF9IzFTWE3QWmbm5Nlf_wPoXwgbGFMM8bUQ&usqp=CAU")
    await UserState.fullname.set()

@dp.message_handler(content_types="text",state=UserState.first())
async def get_fullname(message:Message,state:FSMContext):
    ism=message.text
    await state.update_data(fullname=ism)#{"fullname":"Alisher"}
    await message.reply("Telefon raqamni kirit")
    await UserState.next()

@dp.message_handler(content_types="text",state=UserState.phone)
async def get_phone(message:Message,state:FSMContext):
    tel=message.text
    data=await state.get_data()
    ism=data["fullname"]
    await message.answer(f"Malumotingiz <code>togrimi</code>\n<b>{ism}</b>\n<i>{tel}</i>")
    await message.answer("<a href='t.me//coder_ali'>Admin</a>")
    await state.finish()
