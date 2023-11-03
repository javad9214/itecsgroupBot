import logging

from telegram import Update

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler)

from UserInput import input_main
from Config import TOKEN
from Strings import WELLCOME

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

product = []


async def start(update, context):
    await update.message.reply_text(WELLCOME)


def main():
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    conversation_handler = input_main()

    application.add_handler(conversation_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
