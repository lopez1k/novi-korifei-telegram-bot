from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery

from utils.requestsbd import get_need_ticket, delete_ticket, check_admin
from utils.keyboards.inline_builder import kb_in_ticket, tickets_kb

from datetime import datetime

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


acall_router = Router()

class Choice(StatesGroup):
    afk = State()
    answer = State()
    delete = State()


@acall_router.callback_query(F.data == 'return')
async def return_call(call: CallbackQuery, state: FSMContext):
    if await check_admin(call.from_user.id) == 1:
        await state.clear()
        kb = await tickets_kb()
        await call.message.edit_text(f"<i>Список тікетів станом на</i> <b>{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}</b>", reply_markup=kb)

@acall_router.callback_query(F.data.in_(['answer_to_ticket', 'close_ticket']))
async def ticket_choice(call: CallbackQuery, state: FSMContext, bot: Bot):
    if await check_admin(call.from_user.id) == 1:
        data = await state.get_data()

        if call.data == 'close_ticket':
            tid = data['tid']
            user_id = data['user_id']
            await delete_ticket(tid)
            await call.message.answer(f"<b>Закрито тікет під номером</b> <i>{tid}</i>")
            await bot.send_message(user_id, f"<b>Модератор закрив ваш тікет!</b>")
            await bot.send_message(chat_id = -1001952618666, text = f"<b>Модератор <code>{call.from_user.full_name}</code> закрив тікет під номером {tid}</b>", message_thread_id = 1291)
            

        elif call.data == 'answer_to_ticket':
            await call.message.answer('Введіть відповідь користувачу:')
            await state.set_state(Choice.answer)
    
        await call.answer()

@acall_router.message(Choice.answer)
async def answer_to_ticket(msg: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    user_id = data['user_id']
    await bot.send_message(user_id, f"<b>Відповідь від модератора:</b> <code>{msg.from_user.full_name}</code>\n\n<i>{msg.text}</i>")
    await state.clear()
    await msg.answer("Ви відповили користувачу!", show_alert = True)
    await bot.send_message(chat_id = -1001952618666, text = f"<b>Модератор <code>{msg.from_user.full_name}</code> відповів на тікет. Відповідь: <code>{msg.text}</code></b>", message_thread_id = 1291)
        

@acall_router.callback_query(F.data.startswith("ti_"))
async def take_ticket_by_admin(call:CallbackQuery, state: FSMContext):
    if await check_admin(call.from_user.id) == 1:
        p = await get_need_ticket(int(call.data[3:]))
        await call.message.edit_text(f"📌<b>ID тікета:</b> <i>{p[0]}</i>\n\n👨‍🦱<b>Користувач:</b> <i>{p[2]} | {p[3]}</i>\n\n\n📖<b>Заголовок:</b> <i>{p[4]}</i>\n\n<b>Статус:</b> <i>{p[5]}</i>", reply_markup = kb_in_ticket)
        await state.set_state(Choice.afk)
        await state.update_data(tid = int(call.data[3:]), user_id = p[1])
    


