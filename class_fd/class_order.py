from datetime import datetime
# pour reset là où chercher mes modules s'il y a une erreur avec une chemin relatif
# import sys
# path_cl = 'C://Users/vince/Documents/Université/M1/Programming Basics/Python_Class_Cal_Counter-main/'
# sys.path.append(path_cl)

from exeption import *
from exeption.Exeption_cal_counter import MealTooBigError
from exeption.Exeption_cal_counter import OrderRejectedItemInvalid
from function.fc_meal2000 import F_MealTooBig
from function.import_files_uni import *
from function.cal_counter_no_dict_input import *
from function.cal_counter_with_dict_input import *


class Order:
    """
    This class represents an order.

    Arguments:
        items (list): A list of item ids.
        date (datetime): The date and time of the order.

    Class attributes:
        counter (int): A counter for the number of orders.

    Attributes:
        order_id (str): A unique identifier for the order.
        order_accepted (bool): Whether or not the order was accepted.
        order_refused_reason (str): The reason the order was refused.
        date (datetime): The date and time of the order.
        items (list): A list of item ids.

    Properties:
        calories (int): The total calories for the order.
        price (int): The total price for the order.
    """
    counter = 0

    def __init__(self, items, date=None):
        # i want the order id to be = ID_n°x_date(sep=.)
        # et le x se reset tous les jours
        self.order_id: str = "ID_n°" + str(datetime.today())
        self.date = datetime.today()
        self.order_refused(items)
        self.items = items
        self.order_accepted = True
        self.order_refused_reason = None
        self._calories = None
        self._price = None

    @staticmethod
    def order_refused(*items):
        sum_cal_check, price_check = cal_counter_no_dict_input(*items)
        if sum_cal_check > 2000:
            raise MealTooBigError
        if sum_cal_check == 0 and price_check == 0:
            raise

    @property
    def cal_price(self):
        sum_cal_check, price_check = cal_counter_no_dict_input(self.items)
        self._calories = sum_cal_check
        self._price = price_check
        return self

    def _get_items(self):
        print(f"\nOrder Items = {self.items}\n/////{self.order_id}\n")
        return self.items

    def _get_id(self):
        print(f"\nOrder ID = {self.order_id}\n")
        return self.order_id

    def _get_calories(self):
        print(f"\nOrder Calories = {self._calories}\n/////{self.order_id}\n")
        return self._calories

    def _get_price(self):
        print(f"\nOrder Price = {self._price}\n/////{self.order_id}\n")
        return self._price

    def _set_calories(self, sum_cal):
        self._calories = sum_cal
        return self._calories

    def _set_price(self, price_tt):
        self._price = price_tt
        return self._price

    def summary(self):
        print(f"//////{self.order_id}\nOrder Items = {self.items}\nOrder Price = {self._price}\nOrder Calories = {self._calories}\n//////")
        pass
