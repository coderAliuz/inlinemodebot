from aiogram import Bot,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

token=""
bot=Bot(token,parse_mode=ParseMode.HTML)
dp=Dispatcher(bot,storage=MemoryStorage())