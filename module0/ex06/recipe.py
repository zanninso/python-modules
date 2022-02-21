

from curses.ascii import isdigit
from os import system
import re

from numpy import delete


cookbook = {}


def add_recipe(name, ingredients, meal, prep_time):
    if (name in cookbook):
        print()
    else:
        cookbook[name] = [ingredients, meal, prep_time]


def delete_recipe(name):
    if (name in cookbook):
        del cookbook[name]


def print_recipe(name):
    if (name in cookbook):
        print("Recipe for {}:".format(name))
        print("Ingredients list {}:".format(cookbook[name][0]))
        print("To be eaten for {}.".format(cookbook[name][1]))
        print("Takes {} minutes of cooking.".format(cookbook[name][2]))
    else:
        print("Recipe {} not registred".format(name))


def print_cookbook():
    for recipe in cookbook:
        print(recipe)


def exit_cookbook():
    exit()


def input_block():
    input("\npress anything to back to menu...")
    system('clear')


add_recipe('sandwich', ['ham', 'bread', 'cheese', 'tomatoes'], 'lunch', 10)
add_recipe('cake', ['flour', 'sugar', 'eggs'], 'dessert', 60)
add_recipe('salad', ['avocado', 'arugula', 'tomatoes', 'spinach'], 'lunch', 15)
system('clear')
while(True):
    resp = input("""Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit
>> """)
    if (resp.isdigit()):
        resp = int(resp)
        if (resp == 1):
            name = input("recipe name: ")
            ingredients = input("recipe ingredients: ").split()
            meal = input("recipe meal type: ")
            prep_time = input("recipe prepaation time: ")
            while(prep_time.isdigit() is False or int(prep_time) < 0):
                prep_time = input("recipe prepaation time: ")
            add_recipe(name, ingredients, meal, int(prep_time))
        elif(resp == 2):
            name = input("Please enter the recipe's name to delete: ")
            delete_recipe(name)
        elif(resp == 3):
            name = input("Please enter the recipe's name to get its details: ")
            print_recipe(name)
        elif (resp == 4):
            print_cookbook()
        elif (resp == 5):
            exit_cookbook()
        else:
            print("This option does not exist, \
please type the corresponding number.")
        input_block()
    else:
        print("This option it's not correct, \
please type just a number from 1 to 5")
        input_block()
