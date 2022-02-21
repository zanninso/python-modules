from datetime import datetime
import re
from recipe import *


class book():
    def __init__(self, name):
        res, err = check_types({'name': (name, str)})
        if (res is False):
            exit(print(err))

        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {'starter': {}, 'lunch': {}, 'dessert': {}}

    def get_recipe_type_by_name(self, name):
        res, err = check_types({'name': (name, str)})
        if (res is False):
            exit(print(err))

        for recipe_type in self.recipes_list:
            if name in self.recipes_list[recipe_type]:
                return recipe_type
        return None

    def get_recipe_by_name(self, name):
        res, err = check_types({'name': (name, str)})
        if (res is False):
            exit(print(err))

        """Prints a recipe with by name and returns the instance"""
        recipe_type = self.get_recipe_type_by_name(name)
        if (recipe_type is None):
            print("recipe not found")
            return
        print(self.recipes_list[recipe_type][name])
        return self

    def get_recipes_by_types(self, type):
        res, err = check_types({'type': (type, str)})
        if (res is False):
            exit(print(err))

        """Get all recipe names for a given recipe_type """
        if (type in self.recipes_list):
            return([recipe for recipe in self.recipes_list[type]])
        print('error in get_recipes_by_types type {} not found'.format(type))
        return([])

    def add_recipe(self, rcp_obj):
        """Add a recipe to the book and update last_update"""

        res, err = check_types({'recipe_obj': (rcp_obj, recipe)})
        if (res is False):
            exit(print(err))

        if (rcp_obj.recipe_type in self.recipes_list):
            self.recipes_list[rcp_obj.recipe_type][rcp_obj.name] = rcp_obj
            self.last_update = datetime.now()
        return self
