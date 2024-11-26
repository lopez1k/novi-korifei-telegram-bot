from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.requestsbd import get_spect, get_tickets, create_request_ticket

async def spectacls():
    tickets = await get_spect()
    keyboard = InlineKeyboardBuilder()
    for record in tickets:
        keyboard.button(text = record[1], callback_data=f"spect_{record[0]}")
    keyboard.adjust(2)
    return keyboard.as_markup()
        

async def feed(name):
    feedback = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text = "Залишити відгук про виставу", callback_data = f"feedback_{name}")
            ]
        ]
    )
    return feedback

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
                InlineKeyboardButton(text = "💵Придбати💵", callback_data = f"buy_{name}")
            ],
            [InlineKeyboardButton(text = "Повернутись", callback_data = "return_to_spect")]
        ]
    )
    return buy_kb

async def aceppt_kb(id, uid):
    id = await create_request_ticket(id, uid)
    buy_kb = InlineKeyboardMarkup(
        inline_keyboard= [
            [
                InlineKeyboardButton(text = "✅Підтвердити✅", callback_data = f"acct_{id}"),
                InlineKeyboardButton(text = "❌Відхилити❌", callback_data = f"dect_{id}")
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
            InlineKeyboardButton(text = 'Instagram', url = 'https://www.instagram.com/novikorifei/'),
            InlineKeyboardButton(text = 'Facebook', url = 'https://www.facebook.com/people/Театральна-студія-Нові-корифеї/61559699540927/')
        ],
        [
            InlineKeyboardButton(text = 'Telegram', url = 'https://t.me/novikorifei'),
            InlineKeyboardButton(text = 'Gmail', url = 'https://mail.google.com/mail/u/0/?fs=1&to=novikorifei@gmail.com&tf=cm')
        ]
    ]
)