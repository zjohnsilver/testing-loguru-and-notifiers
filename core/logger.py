import sys
from loguru import logger
from .notify import telegram_handler

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