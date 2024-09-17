import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

a = len(names)
random_integer = random.randint(0,a-1)
b = names[random_integer]

print(b + " is going to buy the meal today!")