from itecsgroupBot.constants.strings import Strings
from itecsgroupBot.utils.price_formatter import formate_price


class Product:
    def __init__(self):
        self.name = None
        self.price = None
        self.author = None
        self.date = None
        self.category = None
        self.description = None

    def __str__(self):
        return (f"{Strings.Product.NAME} : {self.name}\n"
                f"{Strings.Product.PRICE} : {formate_price(self.price)}\n"
                f"{Strings.Product.AUTHOR} : {self.author}\n"
                f"{Strings.Product.DATE} : {self.date}\n"
                f"{Strings.Product.CATEGORY} : {self.category}\n"
                f"{Strings.Product.DESCRIPTION} : {self.description}\n")
