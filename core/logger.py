import sys
from loguru import logger
from .notify import telegram_handler, gmail_handler

logger.remove()

logger.add(
    sys.stdout,
    colorize=True,
    format=(
        "<green>{time:YYYY-MM-DD at HH:mm:ss}</green>"
        " | <level>{message}</level>"
    ),
)

logger.add(
    telegram_handler,
    format=("{message}"),
    level="ERROR",
)

logger.add(
    gmail_handler,
    format=("{message}"),
    level="ERROR",
)
