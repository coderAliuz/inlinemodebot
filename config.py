from aiogram import Bot,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

admin=5906451521
token=""
bot=Bot(token,parse_mode=ParseMode.HTML)
dp=Dispatcher(bot,storage=MemoryStorage())