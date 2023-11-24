# pour reset là où chercher mes modules
# import sys
# path_cl = 'C://Users/vince/Documents/Université/M1/Programming Basics/Python_Class_Cal_Counter-main/'
# sys.path.append(path_cl)

from exeption.Exeption_cal_counter import MealTooBigError
from function.fc_meal2000 import F_MealTooBig
from function.import_files_uni import *


def cal_counter_no_dict_input(*args):

    sum_cal: int = 0
    price: int = 0
    list_final: list = []
    for y in args:
        if type(y) == list:
            list_final = y
        else:
            list_final.append(y)

    for plat in list_final:
        for d_meals in meals:
            if plat in d_meals.values():
                    F_MealTooBig(d_meals['calories'])
                    sum_cal = sum_cal + d_meals['calories']
                    price = price + d_meals['price']

        for d_combo in combos:
            if plat in d_combo.values():
                price = price+d_combo['price']
                for meals_combos in d_combo['meals']:
                    for i in meals:
                        if i['id'] == meals_combos:
                            F_MealTooBig(i['calories'])
                            sum_cal = sum_cal + i["calories"]
    # print('CCNDI ---------------\n',"Cal n° =", sum_cal,"Price =", price,'\n---------------------')
    return sum_cal, price
