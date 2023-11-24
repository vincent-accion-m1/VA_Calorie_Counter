from exeption.Exeption_cal_counter import MealTooBigError


def F_MealTooBig(meal_cal: int):
    if meal_cal > 2000:
        raise MealTooBigError
    return MealTooBigError
