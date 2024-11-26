from aiogram import F, Router
from aiogram.types import CallbackQuery
from utils.requestsbd import get_cur_spect
from utils.keyboards.inline_builder import spectacls, return_kb
from datetime import datetime

spect_callback = Router()


@spect_callback.callback_query(F.data.startswith("spect_"))
async def change_spect(call: CallbackQuery):
    spects = await get_cur_spect(call.data[6:])
    await call.message.edit_text(text = f"<b>📋Назва:</b> <i>{spects[1]}</i>\n\n<b>📄Опис:</b> <i>{spects[2]}</i>\n\n<b>📍Місце проведення:</b> <i>{spects[3]}</i>\n\n<b>📅Дата:</b> <i>{spects[4]}</i>", reply_markup = return_kb)

@spect_callback.callback_query(F.data == "return_to_spect")
async def list_of_spect(call: CallbackQuery):
    kb = await spectacls()
    time = datetime.now()
    now_time = time.strftime("%d-%m-%y %H:%M:%S")
    await call.message.edit_text(text = f"<i>Найближчі вистави станом на </i><b>{now_time}</b>", reply_markup = kb)

