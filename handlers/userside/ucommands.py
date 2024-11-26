from aiogram import F, Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandObject, CommandStart, Command
from utils.requestsbd import exists_user, get_user_tickets, check_admin
from utils.keyboards.reply_kb import reg_btn, main_kb
from utils.keyboards.inline_builder import spectacls
from datetime import datetime
from data.config import bot_commands, admin_commands



ucoms = Router()

@ucoms.message(CommandStart())
async def start_cmd_user(msg: Message, command: CommandObject):
    if await exists_user(msg.from_user.id) is None:
        await msg.reply(f"Вітаю, {msg.from_user.full_name}. Для реєстрації у боті натисність на кнопку нижче.", reply_markup = reg_btn)
    else:

        if command.args == 'buyticket':
            kb = await spectacls()
            time = datetime.now()
            now_time = time.strftime("%d-%m-%y %H:%M:%S")
            await msg.answer_photo(photo = "https://telegra.ph/file/71f02301ec9deaf902106.jpg", caption= f"<i>Найближчі вистави станом на </i><b>{now_time}</b>", reply_markup = kb)

        elif command.args:
            user_tickets = await get_user_tickets(command.args)
            user_list_text = "Список квитків користувача:\n"
            for id, owner_id, owner_name, owner_phone, spect, date, purchase, accept in user_tickets:
                user_info = f"🎫<b>№</b>: {id} ({owner_id}) | {owner_name}, <b>📱Номер телефону:📱</b> {owner_phone}, <b>🏛Вистава:</b> {spect} на 🕘{date}. 📅Дата покупки: {purchase}🎫, Підтвердив: {accept}\n\n———————————————-\n\n"
                user_list_text += user_info
            await msg.answer(user_list_text, parse_mode="html")
            
        else:
            await msg.reply(text = "Вас вітає команда нових корифеїв.", reply_markup = main_kb)



@ucoms.message(Command('help'))
async def cmd_user(msg: Message, bot: Bot):
    if await check_admin(msg.from_user.id) == 1:
        await bot.set_my_commands(admin_commands)
    else:
        await bot.set_my_commands(bot_commands)