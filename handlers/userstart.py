from aiogram.types import Message,CallbackQuery
from config import dp
from aiogram.dispatcher import FSMContext
from state import UserState,MainState
from keyboards import check_info_kb,main_kb,del_kb
from model import check_users,user_add

@dp.message_handler(commands="start",state="*")
async def start(message:Message,state: FSMContext):
    await state.finish()
    if check_users(message.chat.id):
        await message.answer("Kerakli bo'limni tanlang",reply_markup=main_kb)
        await MainState.main.set()
    else:
        await message.answer("Salom xush kelibsiz\nIsm va Familiyani kiriting",reply_markup=del_kb)
        await UserState.fullname.set()

@dp.message_handler(content_types="text",state=UserState.fullname)
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
    await state.update_data(phone=tel)
    await message.answer(f"Malumotingiz <code>togrimi</code>\n<b>{ism}</b>\n<i>{tel}</i>",reply_markup=check_info_kb)
    # await message.answer("<a href='t.me//coder_ali'>Admin</a>")
    await UserState.next()

@dp.callback_query_handler(text=["yes","no"],state=UserState.check)
async def check_info(call:CallbackQuery,state:FSMContext):
    check=call.data
    if check=="yes":
        
        data=await state.get_data()
        fullname=data["fullname"]
        phone=data["phone"]
        user_add(call.message.chat.id,fullname,phone) #bazaga malumotni yozadi

        await call.message.edit_text("Ma'lumotlaringiz qabul qilindi")
        await call.message.answer("Kerakli bo'limni tanlang",reply_markup=main_kb)
        await state.finish()
        await MainState.main.set()
    else:
        await call.message.edit_text("Ma'lumotlar qabul qilinmadi\nIsm va Familiyani kiriting")
        await UserState.first()


