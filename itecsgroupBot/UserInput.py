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
    ENTER_THE_DESCRIPTION,
    PRODUCT_ADDED_SUCCESSFILLY
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
async def addProduct(update, context) -> int :
    await update.message.reply_text(ENTER_PRODUCT_NAME)


    return PRODUCT_NAME

async def productName(update, context) -> int:
    productNameValue = update.message.text
    logging.info("the name of product is : %s", productNameValue )

    await update.message.reply_text(ENTER_THE_PRICE)


    return PRICE


async def price(update, context) -> int:
    # user = update.message.from_user
    priceValue = update.message.text

    logging.info("the price of product is : %s", priceValue )

    await update.message.reply_text(ENTER_THE_CATEGORY)


    return CATEGORY


async def category(update, context) -> int:
    categoryValue = update.message.text

    logging.info("the category of product is : %s", categoryValue )

    await update.message.reply_text(ENTER_THE_DESCRIPTION)


    return DESCRIPTION

async def description(update, context) -> int:
    descriptionValue = update.message.text

    logging.info("the description of product is : %s", descriptionValue )

    await update.message.reply_text(PRODUCT_ADDED_SUCCESSFILLY)


    return ConversationHandler.END

# Handler for the /cancel command
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Conversation canceled.")
    return ConversationHandler.END

def inputMain():

    # Create a ConversationHandler with states
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('add_product', addProduct)],
        states={
            PRODUCT_NAME: [MessageHandler(filters.TEXT, productName)],
            PRICE: [MessageHandler(filters.TEXT, price)],
            CATEGORY: [MessageHandler(filters.TEXT, category)],
            DESCRIPTION:[MessageHandler(filters.TEXT, description)]

        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    return conversation_handler




