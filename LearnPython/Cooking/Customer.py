from UsefulTools import get_random
from MealType import MealType
from MealOrder import MealOrder

class Customer:
    def __init__(self, fussiness):
        self.fussiness = fussiness
        self.anger = 0
        self.complete = False

    def take_order(self):
        meal = get_random(0, 3)
        self.order = MealOrder(MealType[meal])

    def give_tip(self):
        tip_percentage = 100 - self.anger
        print(f"Restaurant was given {tip_percentage}% tip!")

    def update(self):
        if not(self.complete):
            self.anger += self.fussiness
        elif self.complete:
            self.give_tip()


