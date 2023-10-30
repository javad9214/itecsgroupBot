import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from Strings import (
    ENTER_PRODUCT_NAME,
    ENTER_THE_PRICE,
    ENTER_THE_CATEGORY,
    ENTER_THE_DESCRIPTION
)
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Define states for conversation
PRODUCT_NAME, PRICE, CATEGORY, UPDATE_DATE, DESCRIPTION  = range(5)

# Handler for the /start command
async def start(update, context) -> int :
    await update.message.reply_text(ENTER_PRODUCT_NAME)

    # Transition to the FIRST state
    return PRODUCT_NAME

# Handler for the user's response
async def price(update, context) -> int:
    # user = update.message.from_user
    product_name = update.message.text
    logging.info("the name of product is : %s", product_name )

    await update.message.reply_text(ENTER_THE_PRICE)

    # Transition to the SECOND state
    return PRICE

async def category(update, context) -> int:
    price = update.message.text

    logging.info("the price of product is : %s", price )

    await update.message.reply_text(ENTER_THE_CATEGORY)

    # Transition to the SECOND state
    return CATEGORY

async def description(update, context) -> int:
    category = update.message.text

    logging.info("the price of product is : %s", category )

    await update.message.reply_text(ENTER_THE_DESCRIPTION)

    # Transition to the SECOND state
    return DESCRIPTION

# Handler for the /cancel command
def cancel(update, context):
    update.message.reply_text("Conversation canceled.")
    return ConversationHandler.END

def inputMain():

    # Create a ConversationHandler with states
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            PRODUCT_NAME: [MessageHandler(filters.TEXT, price)],
            PRICE: [MessageHandler(filters.TEXT, category)],
            CATEGORY: [MessageHandler(filters.TEXT, description)],
            DESCRIPTION:[MessageHandler(filters.TEXT, price)]

        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    return conversation_handler




