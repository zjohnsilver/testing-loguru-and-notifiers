from notifiers.logging import NotificationHandler
from .env import TELEGRAM_TOKEN, TELEGRAM_CHANNEL_ID

defaults = {
    "token": TELEGRAM_TOKEN,
    "chat_id": TELEGRAM_CHANNEL_ID,
}

telegram_handler = NotificationHandler("telegram", defaults=defaults)