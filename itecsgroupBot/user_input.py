import telebot

from telebot import types

class UserInputHandler:

    def __init__(self, bot):
        self.bot = bot
        self.product_list = []


    def process_start_step(message, self):
        try:
            sent = self.bot.send_message(message.chat.id, "لطفا نام محصول را وارد کنید ")
            self.bot.register_next_step_handler(sent, self.process_product_step)
        except Exception as e:
             self.bot.reply_to(message, 'مشکلی پیش آمده است.')

    def process_product_step(message, self):
        try:
            name = message.text
            sent = self.bot.send_message(message.chat.id, "لطفا قیمت محصول را به تومان وارد کنید ")
            self.bot.register_next_step_handler(sent, self.process_price_step, name)
        except Exception as e:
            self.bot.reply_to(message, 'مشکلی پیش آمده است.')

    def process_price_step(message, name, self):
        try:
            price = int(message.text)
            formatted_price = "{:,} تومان".format(price)  # Add commas and IRR at the end
            markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.add('موتورخانه', 'چاهک', 'کابین')
            sent = self.bot.send_message(message.chat.id, "لطفا دسته بندی مورد نظر خود را انتخاب نمایید:", reply_markup=markup)
            self.bot.register_next_step_handler(sent, self.process_category_step, name, price)
        except Exception as e:
            self.bot.reply_to(message, 'An error occurred.')

    def process_category_step(message, name, price, self):
        try:
            category = message.text
            sent = self.bot.send_message(message.chat.id, "زمان آخرین بروزرسانی محصول را وارد کنید." , reply_markup=types.ReplyKeyboardRemove())
            self.bot.register_next_step_handler(sent, self.process_update_time_step, name, price,category)
        except Exception as e:
            self.bot.reply_to(message, 'مشکلی پیش آمده است.')

    def process_update_time_step(message, name, price, category, self):
        try:
            update_time = message.text
            sent = self.bot.send_message(message.chat.id, "نام مرجع محصول را وارد کنید.")
            self.bot.register_next_step_handler(sent, self.process_reference_step, name, price,category, update_time)
        except Exception as e:
            self.bot.reply_to(message, 'مشکلی پیش آمده است.')

    def process_reference_step(message, name, price, category, update_time, self):
        try:
            reference = message.text
            sent = self.bot.send_message(message.chat.id, "توضیحات محصول را وارد کنید.")
            self.bot.register_next_step_handler(sent, self.process_description_step, name, price, category, update_time, reference, self)
        except Exception as e:
            self.bot.reply_to(message, 'مشکلی پیش آمده است.')

    def process_description_step(message, name, price, category, update_time, reference, self):
        try:
            description = message.text

            product = {'name': name,
                    'price': price,
                    'category': category,
                    'update_time': update_time,
                    'reference': reference,
                    'description': description}

          
            self.product_list.append(product)
            self.bot.reply_to(message, 'محصول با موفقیت به لیست اضافه شد.')


        except Exception as e:
            self.bot.reply_to(message, 'مشکلی پیش آمده است.')

    def get_product_list(self):
        return self.product_list