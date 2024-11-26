from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
import asyncio
from utils.create_db import CreateDB
from handlers.userside import ucommands, other_handler, closest_spect, payment
from handlers.adminside import acommands, callback
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils.delete_spect import interval_message
from aiogram.fsm.storage.redis import RedisStorage
import logging
from data.config import api_token



logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('app.log', mode='a', encoding='utf-8')  
    ]
)

async def main():
    scheduler = AsyncIOScheduler(timezone = "Europe/Kyiv")
    bot = Bot(api_token, default = DefaultBotProperties(parse_mode="html")) 
    dp = Dispatcher(storage=RedisStorage.from_url('redis://localhost:6379/0'))
    dp.include_routers(ucommands.ucoms, 
                       other_handler.uohandle, 
                       closest_spect.spect_callback, 
                       acommands.acom_router, 
                       callback.acall_router, 
                       payment.payment_rt)
    scheduler.add_job(interval_message, trigger= 'interval', hours = 5, args=[bot])
    await interval_message(bot)
    scheduler.start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    CreateDB()
    print("start")
    


if __name__ == "__main__":
    asyncio.run(main())