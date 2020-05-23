from Chef import Chef
from MealType import MealType
import random


class InternChef(Chef):
    def make_veg_dish(self):
        if self._random_success() == True:
            super().make_veg_dish()
        else:
            return False

    def make_meat_dish(self):
        if self._random_success() == True:
            super().make_veg_dish()
        else:
            return False

    def make_soup_dish(self):
        if self._random_success() == True:
            super().make_veg_dish()
        else:
            return False

    def make_bread_dish(self):
        if self._random_success() == True:
            super().make_veg_dish()
        else:
            return False

    def _random_success(self):
        return random.randint(1, 10) >= 7
