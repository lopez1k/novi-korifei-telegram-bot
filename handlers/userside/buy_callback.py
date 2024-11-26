from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery
from utils.requestsbd import get_cur_spect, get_tickets_count, create_offer
from utils.keyboards.inline_builder import buy_kb, aceppt_kb
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

buy_callback = Router()

@buy_callback.callback_query(F.data.startswith("ticket_"))
async def change_spect(call: CallbackQuery):
    spects = await get_cur_spect(call.data[7:])
    tickets = await get_tickets_count(spects[1])
    buy = await buy_kb(spects[1])
    if tickets[0] == 0:
        await call.message.edit_text(text = f"Name: {spects[1]}\nFree tickets: {tickets[0]}")
    else:
        await call.message.edit_text(text = f"Name: {spects[1]}\nFree tickets: {tickets[0]}", reply_markup = buy)



@buy_callback.callback_query(F.data.startswith("buy_"))
async def sell_kb_handler(call: CallbackQuery, bot: Bot):
    id = await create_offer(call.data[4:], "232", call.from_user.id)
    await call.message.reply("Очікуйте підтвердження...")
    kb = await aceppt_kb(id)
    await bot.send_message(chat_id = -1001952618666, text = f"{call.from_user.full_name} придбав квиток на виставу {call.data[4:]}", message_thread_id=1291, reply_markup = kb)


