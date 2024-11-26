from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


reg_btn = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "Відправити контакт", request_contact=True)
        ]
    ],
    resize_keyboard = True
)



main_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "Про нас"),
            KeyboardButton(text = "Залишити запитання")
        ],
        [
            KeyboardButton(text = "Найближчі вистави")
        ]
    ], 
    resize_keyboard = True
)