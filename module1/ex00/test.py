from numpy import rec
from recipe import recipe
from book import book


cookbook = book("cookbook")

cookbook.add_recipe(recipe('salad', 2, 15, ['t', 'f', 's'], 'starter'))
cookbook.add_recipe(recipe('cake', 3, 45, ['egg', 'sugar', 'm'], 'dessert'))
cookbook.add_recipe(recipe('tacos', 1, 15, ['30dh'], 'lunch'))
cookbook.add_recipe(recipe('tacos-xl', 1, 15, ['50dh'], 'lunch'))
cookbook.add_recipe(recipe('tacos-xl', 1, 15, ['50dh'], 'lunch'))

print('starter recipe:')
for recipe_name in cookbook.get_recipes_by_types('starter'):
    cookbook.get_recipe_by_name(recipe_name)
print()

print('lunch recipe:')
for recipe_name in cookbook.get_recipes_by_types('lunch'):
    cookbook.get_recipe_by_name(recipe_name)
print()

print('test recipe:')
for recipe_name in cookbook.get_recipes_by_types('test'):
    cookbook.get_recipe_by_name(recipe_name)
print()

cookbook.get_recipe_by_name("not found")

cookbook.add_recipe("not recipe")
