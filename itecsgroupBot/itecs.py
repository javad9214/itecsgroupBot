# -*- coding: utf-8 -*-

import telebot
import mysql.connector
import logging
import datetime

from telebot import types

logging.basicConfig(filename='myapp.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


bot = telebot.TeleBot("6010757760:AAFhe2OKrao_2xib-hcGv49L_ha5kyabQsY")


db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'mjavadse_main_user',
    'password': 'dX{XF[.2.4}9',
    'database': 'mjavadse_mybot'
}


product_list = []

try:
    # Attemt to establish a connection to the database
    connection = mysql.connector.connect(**db_config)
    print("Successfully connected to database!")

except mysql.connector.Error as err:
    print("Error : %s" , err)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "به بات گروه آیتکس خوش آمدید!")

@bot.message_handler(commands=['add_product'])
def add_product(message):
    sent = bot.send_message(message.chat.id, "لطفا نام محصول را وارد کنید ")
    bot.register_next_step_handler(sent, process_product_step)

def process_product_step(message):
    try:
        name = message.text
        sent = bot.send_message(message.chat.id, "لطفا قیمت محصول را به تومان وارد کنید ")
        bot.register_next_step_handler(sent, process_price_step, name)
    except Exception as e:
        bot.reply_to(message, 'مشکلی پیش آمده است.')

def process_price_step(message, name):
    try:
        price = int(message.text)
        formatted_price = "{:,} تومان".format(price)  # Add commas and IRR at the end
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('موتورخانه', 'چاهک', 'کابین')
        sent = bot.send_message(message.chat.id, "لطفا دسته بندی مورد نظر خود را انتخاب نمایید:", reply_markup=markup)
        bot.register_next_step_handler(sent, process_category_step, name, price)
    except Exception as e:
        bot.reply_to(message, 'An error occurred.')

def process_category_step(message, name, price):
    try:
        category = message.text
        sent = bot.send_message(message.chat.id, "زمان آخرین بروزرسانی محصول را وارد کنید." , reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(sent, process_update_time_step, name, price,category)
    except Exception as e:
        bot.reply_to(message, 'مشکلی پیش آمده است.')

def process_update_time_step(message, name, price, category):
    try:
        update_time = message.text
        sent = bot.send_message(message.chat.id, "نام مرجع محصول را وارد کنید.")
        bot.register_next_step_handler(sent, process_reference_step, name, price,category, update_time)
    except Exception as e:
        bot.reply_to(message, 'مشکلی پیش آمده است.')

def process_reference_step(message, name, price, category, update_time):
    try:
        reference = message.text
        sent = bot.send_message(message.chat.id, "توضیحات محصول را وارد کنید.")
        bot.register_next_step_handler(sent, process_description_step, name, price, category, update_time, reference)
    except Exception as e:
        bot.reply_to(message, 'مشکلی پیش آمده است.')

def process_description_step(message, name, price, category, update_time, reference):
    try:
        description = message.text


         # Insert the product into the database
        cursor = connection.cursor()

        insert_query = "INSERT INTO products (name, price, update_time, reference, category, description) VALUES (%s, %s, %s, %s, %s, %s)"
        product_data = (name, price, update_time, reference, category, description)
        cursor.execute(insert_query, product_data)

        connection.commit()
        cursor.close()
        connection.close()


        product = {'name': name,
                   'price': price,
                   'category': category,
                   'update_time': update_time,
                   'reference': reference,
                   'description': description}
        product_list.append(product)
        bot.reply_to(message, 'محصول با موفقیت به لیست اضافه شد.')
    except Exception as e:
        logging.error('error in process-description %s', e)
        print("Error is : " , e)
        bot.reply_to(message, 'مشکلی پیش آمده است.')

@bot.message_handler(commands=['list_products'])
def list_products(message):
    if len(product_list) == 0:
        bot.reply_to(message, 'هیچ محصولی وجود ندارد.')
        return
    for product in product_list:
        text = "نام: {}\n \n  قیمت: {}\n  \nدسته بندی: {}\n \nزمان آخرین بروزرسانی: {}\n\n نام مرجع: {}\n \nتوضیحات: {}\n\n".format(
            product['name'], product['price'],product['category'], product['update_time'], product['reference'], product['description']
        )
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)