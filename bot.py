from aiogram import executor
import logging
from config import dp
import handlers
logger = logging.getLogger(__name__)

# logging.basicConfig(
# 		filename = 'app.log', 
# 		level = logging.WARNING,
# 		format = '%(levelname)s:%(asctime)s:%(message)s'
#         )

logging.basicConfig(level=logging.INFO)

if __name__=="__main__":
    executor.start_polling(dp)