from MealType import MealType


class Chef:
    def __init__(self, name, experience_years, station, busy=0):
        self.name = name
        self.experience = experience_years
        self.meal_speciality = MealType
        self.busy = busy

    def make_veg_dish(self):
        if self.meal_speciality == MealType.Veg or self.experience_years >= 6:
            return True
        else:
            return False

    def make_meat_dish(self):
        if self.meal_speciality == MealType.Meat or self.experience_years >= 3:
            return True
        else:
            return False

    def make_soup_dish(self):
        if self.meal_speciality == MealType.Soup or self.experience_years >= 1:
            return True
        else:
            return False

    def make_bread_dish(self):
        if self.meal_speciality == MealType.Bread or self.experience_years >= 2:
            return True
        else:
            return False

    def update(self):
        if self.busy <= 0:
            print(f"I'm {self.name} and I'm free to do a task")
