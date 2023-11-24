from function.cal_counter_with_dict_input import cal_counter_with_dict_input
from function.cal_counter_no_dict_input import cal_counter_no_dict_input
from class_fd.class_order import Order
# necessary to use 'import *' or it would defeat
# the modularity of "import_files_uni"
from function.import_files_uni import *

# Step 0 : to import data from .json files

# Step 1 : INPUT of a random list of meals, of which we wish to count
# the price and calories
items_list = ['meal-7', 'meal-5', 'lemonade']

# Step 2 : Initalize the input as a "Order" Class
order_test: Order = Order(items=items_list)
# using the summary() function to have an overview of the input
# before calculation
order_test.summary()

# Step 3 : Use the method of the class to add a price and calorie
# count to the instance of the class of the input
order_test.cal_price
# using the previous function to see what has been changed and added
# to the class after calculations
order_test.summary()


#########
# Another way of doing it, is accessing the functions directly

sum_cal_ndi, price_ndi = cal_counter_no_dict_input(order_test._get_items())
order_test._set_calories(sum_cal_ndi)
order_test._set_price(price_ndi)
order_test.summary()

# This way we can also change the base database (in the case of a
# situation with different prices or different menu options)

# (this would need other .json files that would be imported automatically
# anyway thanks to STEP 0)

sum_cal_wdi, price_wdi = cal_counter_with_dict_input(
    meals, combos, order_test._get_items())
order_test._set_calories(sum_cal_wdi)
order_test._set_price(price_wdi)
order_test.summary()
