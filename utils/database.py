__author__ = "Pinkas Matěj - Pinki"
__maintainer__ = "Pinkas Matěj - Pinki"
__email__ = "pinkas.matej@gmail.com"
__credits__ = []
__created__ = "24/04/2025"
__date__ = "24/04/2025"
__status__ = "Prototype"
__version__ = "0.1.0"
__copyright__ = ""
__license__ = ""

"""
Project: ChefMate
Filename: database.py
Directory: utils/
"""

import os
import json
import datetime


class IngredientObject:
    def __init__(self):
        self.name = None
        self.shop = None
        self.stored_home = None
        self.amount = None

    def to_json(self):
        ingredient_json = {}

        for key in self.__dict__.keys():
            ingredient_json[key] = getattr(self, key)

        return ingredient_json


class IngredientBookObject:
    def __init__(self):
        self.ingredient_list = []

    def to_json(self):
        list_json = []
        for item in self.ingredient_list:
            list_json.append(item.to_json())

        return list_json

    def add_ingredient(self, ingredient: IngredientObject):
        self.ingredient_list.append(ingredient)


class RecipeObject:
    def __init__(self):
        self.name = None
        self.ingredients = None
        self.procedure = None
        self.difficulty = None
        self.prep_time = None
        self.cook_time = None
        self.total_time = None
        self.directions = None

    def to_json(self):
        recipe_json = {}

        for key in self.__dict__.keys():
            if hasattr(getattr(self,key), 'to_json'):
                recipe_json[key] = getattr(self,key).to_json()
            else:
                recipe_json[key] = getattr(self, key)

        return recipe_json

    def load_from_json(self, json_string):

        for attribute in json_string:
            if hasattr(self, attribute):
                setattr(self, attribute, json_string[attribute])


class RecipeBookObject:
    def __init__(self):
        self.recipe_list = []

    def add_recipe(self, recipe: RecipeObject):
        self.recipe_list.append(recipe)

    def load_from_json_list(self, recipe_json_list):
        for recipe in recipe_json_list:
            new_recipe = RecipeObject()
            new_recipe.load_from_json(recipe)

            self.recipe_list.append(new_recipe)




class CookBook:
    def __init__(self):
        self.json_data = None
        self.filename = '../data/database.json'

        self.recipe_book = RecipeBookObject()
        self.ingredient_book = IngredientBookObject()

        self.load_from_json()

    def init_json(self):
        created = datetime.datetime.today().strftime('%d/%m/%Y')

        json_string = {
            "version": "0.1.0",
            "created": created,
            "ingredients": [],
            "recipes": []
        }

        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(json_string, f, ensure_ascii=False, indent=4)

    def load_from_json(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            self.json_data = json.load(f)

        self.recipe_book.load_from_json_list(self.json_data['recipes'])

    def save_to_json(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.json_data, f, ensure_ascii=False, indent=4)





    def from_json_to_class_recipe(self, by_value, value):
        for recipe_json in self.json_data['recipes']:
            if recipe_json[by_value] == value:
                recipe_obj = RecipeObject()
                for key in recipe_json.keys():
                    setattr(recipe_obj, key, recipe_json[key])

                return recipe_obj

    def get_songs_names(self):
        names = []
        for library_song in self.json_data['songs']:
            names.append(library_song['name'])
        return names


if __name__ == "__main__":
    cook_book = CookBook()



    print('')


    """book = RecipeBookObject()

    mleko = IngredientObject()
    mleko.name = 'Mléko'

    vejce = IngredientObject()
    vejce.name = 'Vejce'

    recipe = RecipeObject()
    recipe.name = 'Palačinky'
    recipe.ingredients = IngredientListObject()
    recipe.ingredients.ingredient_list = [mleko, vejce]
    recipe.procedure = None
    recipe.difficulty = None
    recipe.prep_time = None
    recipe.cook_time = None
    recipe.total_time = None
    recipe.directions = None

    book.add_recipe(recipe)"""






