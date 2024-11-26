from aiogram import Bot, Dispatcher
import asyncio
from utils.create_db import CreateDB
from handlers.userside import ucommands, other_handler, closest_spect
from handlers.adminside import acommands, callback
from aiogram.fsm.storage.memory import MemoryStorage
import os


async def main():
    bot = Bot(token=os.getenv("TOKEN"), parse_mode="html")
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(ucommands.ucoms, other_handler.uohandle, closest_spect.spect_callback, acommands.acom_router, callback.acall_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    CreateDB()


if __name__ == "__main__":
    asyncio.run(main())