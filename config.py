from aiogram import Dispatcher, Bot
# from aiogram.dispatcher import storage
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
TOKEN = config('TOKEN')

ADMIN=(1970278827,1970278827)
bot = Bot(TOKEN)
db = Dispatcher(bot=bot, storage=storage)
