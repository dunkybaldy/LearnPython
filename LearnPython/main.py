from math import *
import random

##### STRINGS

# number = 2
#
# phrase = "This is  a PHRASE"
# print(phrase.lower())
# print(len(phrase))
# print(phrase[0])
# print(phrase.index("PHRASE")) # where the target string starts
# print(phrase.replace("a", "the"))

##### NUMBERS

# print (10 % 3) # 10 / 3 -> spit out the remainder
# print(str(23)) # this number is actually a string on print
# print(str(5) + " is my fav number") # concatenating numbers and strings
# my_num = -10
# print(my_num)
# print(abs(my_num))
# print(pow(3, 2)) # 3^2
# print(max(1, 50)) # which of the 2 numbers is higher
# print(round(3.5))
# print(round(3.49999999))
# # Required: from math import *
# print(floor(3.9999))
# print(ceil(3.11111))
# print(sqrt(36))
# num1 = input("Enter a number: ")
# num2 = input("Enter a number: ")  # num2 and num1 are both strings
# print(float(num1) + float(num2))  # Casting to a number type

##### USER INPUT

# username = input("Enter your username: ")
# password = input("Enter your password: ")
# print(f"Your name is {username} and your password is {password}")

##### PASSWORD GENERATOR

# s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# passlen = 8
# p =  "".join(random.sample(s,passlen ))
# print(p)

# available_chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# password_length = input("Length of Password: ")
# password = "".join(random.sample(available_chars, password_length))
# print(password)

##### LISTS

# friends = ['Kevin', 'John', 'Jimmy']
# print(friends)
# print(friends[0])
# print(friends[-1])
# print(friends[1:])
# friends[1] = 'Nobby'
#
# prime_numbers = [1, 3, 5, 7, 11]
# prime_numbers.append(13)
# friends.insert(1, 'Kelly')
# friends.remove('Kelly')
# friends.pop()
# friends.clear()
# friends.extend(prime_numbers)
# print(friends)
#
# prime_numbers.reverse()
# print(prime_numbers)
# prime_numbers.sort()
# print(prime_numbers)

##### TUPLES

# coordsList = [(1, 2), (3, 5)]
# coordinates = (4, 5)  # immutable (cannot be changed)
# print(str(coordinates) + ' ' + str(coordinates[1]))  # tuples are indexed

##### FUNCTIONS


# def say_something(something):
#     print(f"{something}")
#
#
# def say_two_things(something, something_else):
#     print(f"{something} {something_else}")
#     print(something + str(something_else))
#
#
# say_something('Mike')
# say_something(25)
# say_two_things('Mike', 25)
#
#
# def power(number, power):
#     return pow(number, power)
#
#
# result = power(9, 4.5)
# print(result)

##### IF STATEMENTS

# cloudy = input("Is the weather cloudy today? ") == "Yes"
# if cloudy:
#     print("It's cloudy today")
# elif not cloudy:
#     print("It's not cloudy today")
# else:
#     print("I do not know because I haven't been outside today..")
#
# is_male = True
# is_tall = False
# if is_male and is_tall:
#     print("You are a tall male")
# elif is_male or is_tall:
#     print("You are a male or tall or both")
# elif not(is_tall):
#     print("You are definitely short")
# else:
#     print("K")

#####  comparison operators


#  == != >= > <= <

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
#
# print(max_num(1,2,3))

#####  DICTIONARY KEYVALUEPAIRS

# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December"
# }
# print(monthConversions["Nov"])
# print(monthConversions.get("Nov"))
# print(monthConversions.get("Nop"))
# print(monthConversions.get("Nop", "Not a valid key"))

##### LOOPS

# number = 10
# while number > 0:
#     print(f"Hello World\n{number}")
#     number -= 1

# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# print(i) # i = 11

# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(fruit)
#
# for index in range(5):
#     if index == 0:
#         print("First Iteration")
#     else:
#         print("Not First")
#
# for fruit in range(len(fruits)):
#     print(fruits[fruit])


# def raise_to_power_while(base_num, pow_num):
#     current_pow = 1
#     result = base_num
#     while current_pow < pow_num:
#         result *= base_num
#         current_pow += 1
#     return result
#
#
# def raise_to_power_for(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result *= base_num
#     return result
#
#
# print(raise_to_power_while(12, 3))
# print(raise_to_power_for(12, 3))

##### 2D LISTS

# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
#
# print(number_grid)
# print(number_grid[0][0])
#
# for row in number_grid:
#     for column in row:
#         print(column)

'''
sadasd
asd
as
das
das
d
'''

##### ERROR CATCHING

# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:  # Shouldn't use empty except
#     print(err)
# except ValueError:
#     print("Invalid input")
