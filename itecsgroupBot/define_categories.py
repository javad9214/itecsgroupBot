import logging

from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

allowed_admins = [72189079]

# Define states for conversation
PRODUCT_NAME, PRICE = range(2)


async def admin_actions(update, context):
    user_id = update.effective_user.id
    if user_id in allowed_admins:
        await update.message.reply_text("You have access to this command!")
    else:
        await update.message.reply_text("You're not authorized to access this command.")


async def cancel(update, context):
    await update.message.reply_text("Conversation canceled.")
    return ConversationHandler.END


def defin_cat_main():
    # Create a ConversationHandler with states
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('admin_actions', admin_actions)],
        states={
            PRODUCT_NAME: [MessageHandler(filters.TEXT, product_name)],
            PRICE: [MessageHandler(filters.TEXT, price)],
            CATEGORY: [MessageHandler(filters.TEXT, category)],
            DESCRIPTION: [MessageHandler(filters.TEXT, description)]

        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    return conversation_handler
