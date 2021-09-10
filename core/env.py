try:
    from dotenv import load_dotenv, find_dotenv

    load_dotenv(find_dotenv())
except ModuleNotFoundError:
    print("Dotenv not found. Please install modules from requirements.txt...")
else:
    print(".env loaded sucessfully...")

from os import getenv

TELEGRAM_TOKEN=getenv('TELEGRAM_TOKEN')
TELEGRAM_CHANNEL_ID=getenv('TELEGRAM_CHANNEL_ID')