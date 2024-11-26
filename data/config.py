from aiogram.types import BotCommand

TOKEN ="6897314008:AAEAo-Lf3mto9-n91B9C27ym84UU5zDzL-U"
PAYMENT_TOKEN = "410694247:TEST:7af7155a-b63d-4a09-b76f-a80d6e86ce67"
LOG_CHAT = -1001952618666
bot_commands = [
        BotCommand(command="/start", description="Розпочати роботу"),
        BotCommand(command="/help", description="Команди бота")
    ]

admin_commands = [
    BotCommand(command="/help", description="Команди бота"),
    BotCommand(command = "/apanel", description = "Вхід в панель керування"),
    BotCommand(command = "/new_spect", description = "Додати нову виставу")
]