from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.client_kb import gender_markup


class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    gender = State()
    region = State()
    photo = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.name.set()
        await message.answer("Как зовут?")
    else:
        await message.answer('Пиши в лс')


async def load_name(message: types.Message, state: FSMContext):
    if not message.text.isalpha():
        await message.answer('Только буквы')
    else:
        async with state.proxy() as data:  # храниться кеш
            data['name'] = message.text
            data['id'] = message.from_user.id
            data['username'] = f'@{message.from_user.username}'
        await FSMAdmin.next()  # переключатель состояния
        await message.answer('Сколько тебе лет?')


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Пиши цифры')
    elif not 18 < int(message.text) < 99:
        await message.answer('Прости, доступ ограничен')
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMAdmin.next()
        await message.answer('Какого ты пола?', reply_markup=gender_markup)


async def load_gender(message: types.Message, state: FSMContext):
    if not message.text.isalpha():
        await message.answer('Только буквы')
        return
    else:
        async with state.proxy() as data:
            data['gender'] = message.text
    await FSMAdmin.next()
    await message.answer('Откуда ты?')


async def load_region(message: types.Message, state: FSMContext):
    if not message.text.isalpha():
        await message.answer('Только буквы')
        return
    else:
        async with state.proxy() as data:
            data['region'] = message.text
    await FSMAdmin.next()
    await message.answer('Скинь фото')


async def load_photo(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await state.finish()


def reg_hand_anketa(db: Dispatcher):
    db.register_message_handler(fsm_start, commands=['reg'])
    db.register_message_handler(load_name, state=FSMAdmin.name)
    db.register_message_handler(load_age, state=FSMAdmin.age)
    db.register_message_handler(load_gender, state=FSMAdmin.gender)
    db.register_message_handler(load_region, state=FSMAdmin.region)
    db.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])