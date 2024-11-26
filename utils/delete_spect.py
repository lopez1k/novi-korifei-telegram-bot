from sqlite3 import connect
from aiogram import Bot
from datetime import datetime
from data.config import LOG_CHAT
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress
from utils.keyboards.inline_builder import feed

async def interval_message(bot: Bot):
    conn = connect("data/main.db")
    cur = conn.cursor()
    cur.execute("SELECT name, date FROM spectacls")
    result = cur.fetchall()
    for row in result:
        date_string = row[1]
        date = datetime.strptime(date_string, "%d-%m-%Y %H:%M")
        if date < datetime.now():
            cur.execute("SELECT DISTINCT owner_id, owner_name FROM ticket_spect WHERE spect = ?", (row[0],))
            res = cur.fetchall()
            cur.execute("SELECT owner_id, owner_name FROM ticket_spect WHERE spect = ?", (row[0],))
            tickets = cur.fetchall()
            kb = await feed(row[0])
            for uid, name in res:
                with suppress(TelegramBadRequest):
                    await bot.send_message(chat_id = uid, text = f"<b>{name}</b>, <i>були раді Вас бачити на нашій виставі</i> <b>\"{row[0]}\"</b>. Залиште відгук про виставу, натиснувши на кнопку нижче.", reply_markup = kb)  
            await bot.send_message(chat_id= LOG_CHAT, text = f"<b>Користувачів успішно повідомлено про кінець вистави <i>\"{row[0]}\"</i>\nКількість квитків, придбана онлайн: <code>{len(tickets)}</code>. \n\nВидалення вистави з бази даних...</b>", message_thread_id = 1291)
            cur.execute("DELETE FROM spectacls WHERE name = ? and date = ?", (row[0], row[1]))
            cur.execute("DELETE FROM ticket_spect WHERE spect = ?", (row[0],))
            conn.commit()
            conn.close()

