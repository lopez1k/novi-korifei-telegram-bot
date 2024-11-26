from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from utils.requestsbd import exists_user
from utils.keyboards.reply_kb import reg_btn, main_kb
ucoms = Router()

@ucoms.message(CommandStart())
async def start_cmd_user(msg: Message):
    if await exists_user(msg.from_user.id) is None:
        await msg.reply(f"Вітаю, {msg.from_user.full_name}. Для реєстрації у боті натисність на кнопку нижче.", reply_markup = reg_btn)
    else:
        await msg.reply(text = "Вас вітає команда нових корифеїв.", reply_markup = main_kb)
