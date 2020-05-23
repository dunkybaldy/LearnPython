from Chef import Chef
from InternChef import InternChef
from MealType import MealType
from Customer import Customer
from UsefulTools import get_random

meat_chef = Chef("Fat Paul", 8, MealType.Meat)
soup_chef = Chef("Moshrum", 5, MealType.Soup)
bread_chef = Chef("Wheatley", 4, MealType.Bread)
intern_meat_chef = InternChef("Chonker", 1, MealType.Meat)

exit_game = False
max_orders = 5
current_orders = 0

customer = []


def generate_customer():
    return Customer(get_random(1, 10))


while not(exit_game):
    if current_orders < max_orders:
        customer.append(generate_customer())

