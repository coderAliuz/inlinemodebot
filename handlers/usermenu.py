from aiogram.types import Message
from config import dp
from state import MainState
from aiogram.dispatcher import FSMContext
from keyboards import *
from model import data_edit_fullname

@dp.message_handler(text="Ortga",state=MainState.editfullname)
@dp.message_handler(text="Tahrirlash",state=MainState.main)
async def user_edit_info(message:Message):
    await message.reply("Qaysi birini tahrirlash",reply_markup=edit_kb)
    await MainState.edituser.set()

@dp.message_handler(text="Ism va Familiya",state=MainState.edituser)
async def user_edit_fullname(message:Message):
    await message.answer("Yangi ism va familiyani kiriting",reply_markup=back_kb)
    await MainState.editfullname.set()

@dp.message_handler(state=MainState.editfullname,content_types="text")
async def edit_fullname(message:Message):
    fullname=message.text
    data_edit_fullname(message.chat.id,fullname)
    await message.reply("Ism va Familiya yangilandi",reply_markup=edit_kb)
    await MainState.edituser.set()

@dp.message_handler(text="Ortga",state=MainState.edituser)
async def back(message:Message):
    await message.answer("Kerakli bo'limni tanlang",reply_markup=main_kb)
    await MainState.main.set()