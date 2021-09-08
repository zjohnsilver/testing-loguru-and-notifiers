from notifiers.logging import NotificationHandler

defaults = {
    "token": "1702989921:AAFk13Lpzupo9Hls4D4x3F6NFWovszfsK3g",
    "chat_id": "-1001270811373",
}

telegram_handler = NotificationHandler("telegram", defaults=defaults)


gmail_params = {
    "username": "johncarlosilver@gmail.com",
    "password": "EcHDb^5uV*rv@e3oCvPUg",
    "to": "johncarlosilver@gmail.com",
}

gmail_handler = NotificationHandler("gmail", defaults=gmail_params)
