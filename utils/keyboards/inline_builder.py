from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.requestsbd import get_spect, get_tickets

async def spectacls():
    tickets = await get_spect()
    keyboard = InlineKeyboardBuilder()
    for record in tickets:
        keyboard.button(text = record[1], callback_data=f"spect_{record[0]}")
    keyboard.adjust(2)
    return keyboard.as_markup()
        

return_kb = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text = "Повернутись", callback_data = "return_to_spect")
        ]
    ]
)


async def buy_kb(name):
    buy_kb = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton(text = "Придбати", callback_data = f"buy_{name}")
            ]
        ]
    )
    return buy_kb

async def aceppt_kb(id):
    buy_kb = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton(text = "Придбати", callback_data = f"acc_{id}")
            ]
        ]
    )
    return buy_kb









async def tickets_kb():
    tickets = await get_tickets()
    keyboard = InlineKeyboardBuilder()
    for record in tickets:
        keyboard.button(text = record[4], callback_data=f"ti_{record[0]}")
    keyboard.adjust(2)
    return keyboard.as_markup()
        
kb_in_ticket = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = "🎙Відповісти на тікет", callback_data = 'answer_to_ticket'),
            InlineKeyboardButton(text = "❌Закрити тікет", callback_data = 'close_ticket')
        ],
        [
            InlineKeyboardButton(text = "⬅️Назад", callback_data = 'return')
        ]
    ]
)


soc_merezhi = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = 'Instagram', url = 'instagram.com'),
            InlineKeyboardButton(text = 'Facebook', url = 'facebook.com')
        ],
        [
            InlineKeyboardButton(text = 'Twitter', url = 'twitter.com'),
            InlineKeyboardButton(text = 'Site', url = 'google.com')
        ],
        [
            InlineKeyboardButton(text = 'Youtube', url = 'youtube.com')
        ]
    ]
)