from aiogram import executor  # для запуска бота
from handler import client, callback, admin, fsm_anketa, extra
from config import db
import logging

client.reg_client(db)
callback.reg_hand_callback(db)
admin.reg_ban(db)
fsm_anketa.reg_hand_anketa(db)
extra.reg_hand_extra(db)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
    