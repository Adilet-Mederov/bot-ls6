from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3
)

start_button = KeyboardButton("/start")
end_button = KeyboardButton("/end")
quiz_button = KeyboardButton("/quiz")
reg_button = KeyboardButton("/reg")

share_location = KeyboardButton("Share location", request_location=True)
share_contact = KeyboardButton("Share contact", request_contact=True)

start_markup.add(start_button, end_button, quiz_button, reg_button,
                 share_location, share_contact)

gender_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton("Мужчина"),
                                                                                      KeyboardButton("Женщина"),
                                                                                      KeyboardButton("Другое"))