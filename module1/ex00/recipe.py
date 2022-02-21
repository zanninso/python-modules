
def check_types(vars):
    err_msg = 'variable {} except type {} given {}.'
    for var in vars:

        # to check type of list items
        if (vars[var][1] == list):
            if (type(vars[var][0]) is not list):
                return False, err_msg.format(var, list, type(vars[var][0]))
            elif (len(vars[var]) == 3):
                for val in vars[var][0]:
                    res, err = check_types({var + '[]': (val, vars[var][2])})
                    if (res is False):
                        return(res, err)

        # to check simple types
        elif (type(vars[var][0]) is not vars[var][1]):
            return False, err_msg.format(var, vars[var][1], type(vars[var][0]))
    return True, ''


class recipe():
    types = ["starter", "lunch", "dessert"]

    def __init__(self, name, lvl, time, ingredients, type, descr=''):

        param_types = {'name': (name, str),
                       "cooking_lvl": (lvl, int),
                       "cooking_time": (time, int),
                       "ingredients": (ingredients, list, str),
                       "recipe_type": (type, str),
                       "description": (descr, str)}

        result, err = check_types(param_types)

        if (result is False):
            exit(print(err))
        if (lvl > 5 or lvl < 1):
            exit(print('cooking_lvl not in (1, 5)'))
        if (time < 0):
            exit(print("cooking time can't be negative"))
        if (type not in self.types):
            exit(print("recipe type '{}' not in {}".format(type, self.types)))

        self.name = name
        self.cooking_lvl = lvl
        self.cooking_time = time
        self.ingredients = ingredients
        self.recipe_type = type
        self.description = descr

    def __str__(self) -> str:
        txt = "* Recipe for: {}\n".format(self.name)
        txt += "Need level {} to cook it\n".format(self.cooking_lvl)
        txt += "Ingredients list : {}\n".format(self.ingredients)
        txt += "Takes {} minutes of cooking\n".format(self.cooking_time)
        txt += "To be eaten for {}\n".format(self.recipe_type)
        txt += "Description: {}".format(self.description)
        return(txt)
