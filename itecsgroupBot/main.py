import logging

import telebot

import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder , ContextTypes , CommandHandler

from user_input import UserInputHandler
from config import TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)


# bot = telebot.TeleBot(TOKEN)


product = []

async def start(update: Update , context: ContextTypes.DEFAULT_TYPE):
   user_input_handler = UserInputHandler(context)
   await user_input_handler.add_product_start(update , context)

async def addProduct(update: Update , context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text= "product added  !!"
        )

# @bot.message_handler(commands=['add_product'])
# def add_product(message):
#     product = user_input_handler.process_product_step(message)
#     if product is not None:
#         print(product)
#     else:
#         print("product is null")



if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start' , start)
    application.add_handler(start_handler)

    addProduct_handler = CommandHandler('add_product' , addProduct)
    application.add_handler(addProduct_handler)

    application.run_polling()