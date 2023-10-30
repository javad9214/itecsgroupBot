import logging


from telegram import Update

from telegram.ext import (Application)

from UserInput import inputMain
from Config import TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)


# bot = telebot.TeleBot(TOKEN)


product = []

# async def start(update: Update , context: ContextTypes.DEFAULT_TYPE):
#    user_input_handler = UserInputHandler(context , update)
#    await user_input_handler.add_product_start()

# async def addProduct(update: Update , context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(
#         chat_id = update.effective_chat.id,
#         text= "product added  !!"
#         )

# @bot.message_handler(commands=['add_product'])
# def add_product(message):
#     product = user_input_handler.process_product_step(message)
#     if product is not None:
#         print(product)
#     else:
#         print("product is null")




def main():
     # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    conversation_handler = inputMain()

    application.add_handler(conversation_handler)

   # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
