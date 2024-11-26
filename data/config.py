from aiogram.types import BotCommand
from dotenv import load_dotenv
import os

load_dotenv()


api_token = os.getenv("API_TOKEN")
payment_token = os.getenv("PAYMENT_TOKEN")
LOG_CHAT = os.getenv("LOG_CHAT")

bot_commands = [
        BotCommand(command="/start", description="Розпочати роботу"),
        BotCommand(command="/help", description="Команди бота")
    ]

admin_commands = [
    BotCommand(command="/help", description="Команди бота"),
    BotCommand(command = "/apanel", description = "Вхід в панель керування"),
    BotCommand(command = "/new_spect", description = "Додати нову виставу")
]