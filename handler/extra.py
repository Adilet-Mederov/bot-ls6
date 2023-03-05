from aiogram import types,Dispatcher
from config import bot,db

async def echo(massage: types.Message):
    bad_words = ['маты']
    for word in bad_words:
       if word in massage.text.lower().replace(' ', ''):
           await  bot.delete_message(massage.chat.id, massage.message_id)
           await massage.answer(f'Не матерись! @{massage.from_user.full_name}')
#
       if massage.text.startswith('.'):
           await bot.pin_chat_message(massage.chat.id,massage.message_id)
       if massage.text == 'python':
           await bot.send_dice(massage.chat.id)


users = {}
async def python(massage: types.Message):
    user_name = massage.from_user.username
    if user_name:
        user_name = user_name
    else:
        user_name = massage.from_user.first_name
    if massage.from_user.username is not users:
        users[f'@{user_name}'] = massage.from_user.id
        print(users                 )

    else:
        pass


def reg_hand_extra(db:Dispatcher):
    db.register_message_handler(echo)
    db.register_message_handler(python)



