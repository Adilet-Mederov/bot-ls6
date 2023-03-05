from aiogram import types,Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, db
from keyboards.client_kb import start_markup



async def start_handler(massage:types.message):
    await massage.answer('Hello!')
    # await bot.send_message(massage.from_user.id,f'{massage.from_user.first_name}\n'
    #                                             f'Для активации викторины---> /quiz')

    # await massage.answer('Пока что всё!')


# опросник\викторина
async def quiz1(massage:types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next', callback_data='button')
    markup.add(button)

    ques = 'Название Мультфильма?'
    answer = [
        'Маша и Медведь!',
        'Молния Маквин! ',
        'Губка Боб квадратные штаны!',
        'Скуби-Ду!',
        'Не знаю!'
    ]
    photo = open('media/bob7.jpg', 'rb')
    await bot.send_photo(massage.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=massage.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        open_period=12,
        reply_markup=markup
    )


def reg_client(db:Dispatcher):
    db.register_message_handler(start_handler,commands=['start' , 'hello'])
    db.register_message_handler(quiz1,commands=['quiz'])










    # db.register_message_handler(info_hand, commands=['info'])
    # async def info_hand(massage: types.Message):
    #     await massage.answer('Нет инфы!')