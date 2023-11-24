from .fc_meal2000 import F_MealTooBig


def cal_counter_with_dict_input(meals_dict, combos_dict, *args):

    sum_cal: int = 0
    price: int = 0
    list_final: list = []
    for y in args:
        if type(y) == list:
            list_final = y
        else:
            list_final.append(y)

    for plat in list_final:
        for d_meals in meals_dict:
            if plat in d_meals.values():
                F_MealTooBig(d_meals['calories'])
                sum_cal = sum_cal+d_meals['calories']
                price = price+d_meals['price']

        for d_combo in combos_dict:
            if plat in d_combo.values():
                price = price+d_combo['price']
                for meals_combos in d_combo['meals']:
                    for i in meals_dict:
                        if i['id'] == meals_combos:
                            F_MealTooBig(i['calories'])
                            sum_cal = sum_cal+i["calories"]

    print('CCWDI ---------------\n', "Cal n° =", sum_cal, "Price =", price, '\n---------------------')

    return sum_cal, price
