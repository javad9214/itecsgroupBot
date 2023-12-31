import logging

from telegram import Update
from telegram.ext import (
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from constants.strings import Strings
from db.database import write_product_to_db
from model.product import Product
from utils.date import DateTime
from utils.price_formatter import formate_price

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Define states for conversation
PRODUCT_NAME, PRICE, CATEGORY, UPDATE_DATE, DESCRIPTION = range(5)

product = Product()


# Handler for the /start command
async def add_product(update, context) -> int:
    await update.message.reply_text(Strings.UserInput.PRODUCT_NAME)
    return PRODUCT_NAME


async def product_name(update, context) -> int:
    product_name_value = update.message.text
    logging.info("the name of product is : %s", product_name_value)
    product.name = product_name_value
    await update.message.reply_text(Strings.UserInput.PRICE)

    return PRICE


async def price(update, context) -> int:
    # user = update.message.from_user
    price_value = update.message.text

    if not price_value.isdigit():
        await update.message.reply_text(Strings.Error.INVALID_INPUT)
        return PRICE
    else:
        price_value = int(price_value)
        logging.info("the price of product is : %s", formate_price(price_value))
        product.price = price_value
        await update.message.reply_text(Strings.UserInput.CATEGORY)

    return CATEGORY


async def category(update, context) -> int:
    category_value = update.message.text

    logging.info("the category of product is : %s", category_value)
    product.category = category_value
    await update.message.reply_text(Strings.UserInput.DESCRIPTION)

    return DESCRIPTION


async def description(update, context) -> int:
    description_value = update.message.text

    logging.info("the description of product is : %s", description_value)
    product.description = description_value
    user_info = update.message.from_user
    add_product_author(user_info)
    await update.message.reply_text(Strings.UserInput.PRODUCT_ADDED_SUCCESSFULLY)
    return ConversationHandler.END


# Handler for the /cancel command
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Conversation canceled.")
    return ConversationHandler.END


def add_product_author(user_info):
    product_author_value = user_info.first_name
    logging.info("the name of user is : %s", product_author_value)
    product.author = product_author_value
    add_product_register_date()


def add_product_register_date():
    product.date = DateTime.get_current_time()
    logging.info("the time that product saves is : %s ", product.date)
    save_product()


def save_product():
    write_product_to_db(product)


def input_main():
    # Create a ConversationHandler with states
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('add_product', add_product)],
        states={
            PRODUCT_NAME: [MessageHandler(filters.TEXT, product_name)],
            PRICE: [MessageHandler(filters.TEXT, price)],
            CATEGORY: [MessageHandler(filters.TEXT, category)],
            DESCRIPTION: [MessageHandler(filters.TEXT, description)]

        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    return conversation_handler
