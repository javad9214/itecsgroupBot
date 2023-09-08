import telebot
from user_input import UserInputHandler



bot = telebot.TeleBot("6010757760:AAFhe2OKrao_2xib-hcGv49L_ha5kyabQsY")

user_input_handler = UserInputHandler(bot)

product = []

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "به ربات گروه آیتکس خوش آمدید!")

@bot.message_handler(commands=['add_product'])
def add_product(message):
    product = user_input_handler.process_product_step(message)
    if product is not None:
        print(product)
    else:
        print("product is null")



if __name__ == "__main__":
    bot.polling(none_stop=True)