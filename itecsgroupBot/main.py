import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler)

from config import TOKEN
from constants.strings import Strings
from db.database import create_table
from db.database import read_products_from_db
from user_input import input_main

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)


async def start(update, context):
    await update.message.reply_text(Strings.Global.WELLCOME)


async def list_products(update, context):
    products = read_products_from_db()
    for product in products:
        await update.message.reply_text(str(product))


def main():
    # Make Sure Table Exist
    create_table()

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    conversation_handler = input_main()

    application.add_handler(conversation_handler)

    application.add_handler(CommandHandler("list_products", list_products))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
