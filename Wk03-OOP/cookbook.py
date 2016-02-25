# Cookbook classes Week03
# 20160225THU BIOF509 HW
# Wayne Liu


class recipe(object):
    """ A class definition of recipe. The following attributes are supported:

    Attributes:
    name: A string of the recipe name, e.g. key lime pie
    kind: A string of the type of food, e.g. dessert
    ingredients: A list of the ingredient objects required, e.g. egg, milk
    instructions: A string of the amount and steps to prepare and cook the
        ingredients, e.g. mix and bake
    equipment: A list of the equipment needed, e.g. spoon, bowl
    serving_size: An integer for the number of recommended people it can
        serve, e.g. 8
    nutrition: A dictionary of the nutritional facts, e.g. Total calories,
        fat calories
    time: A datetime for cooking time, e.g. 30 minutes"""


    def __init__(self, name, kind, ingredients, instructions, equipment,
                 serving_size, nutrition, time):
        """ Returns a recipe object with name, kind, ingredients, instructions,
        equipment, serving_size, nutrition, and time"""
        self.name = name
        self.kind = kind
        self.ingredients = ingredients
        self.instructions = instructions
        self.equipment = equipment
        self.serving_size = serving_size
        self.nutrition = nutrition
        self.time = time


    def __str__(self):
        """ Returns a basic string representation of the recipe object"""
        return "A {0} called {1}, which serves {2}.".format(
            self.kind, self.name, self.serving_size
        )


    def getNutrition(self):
        """ Returns the all nutrition facts from the ingredient objects"""
        pass


    def scaleServings(self, n):
        """ Returns scaled serving size based on n"""
        pass

pie = recipe("key lime pie", "dessert", ["pie crust", "limes"],
             "mix and bake", "bowl and knife", 4,
             {"fat": "lots", "carbs": "sweet"}, 30.4)
print(pie)
print("How much fat?", pie.nutrition['fat'])


class ingredient(object):
    """ A class definition of a ingredient. The following attributes are supported:

    Attributes:
    name: A string representing the ingredient name, e.g. chicken wings
    nutrition: A dictionary representing grams in each nutrient category,
    e.g. fats, carbs, proteins, vitamins
    amount: A float in grams of the amount of ingredient proportional to
    nutritional facts, e.g. 200.0"""


    def __init__(self, name, nutrition, amount):
        """ Returns a recipe object with name, nutrition, amount"""
        self.name = name
        self.nutrition = nutrition
        self.amount = amount


    def __str__(self):
        """ Returns a basic string representation of the ingredient"""
        return "{0}, has {1} grams of carbs, and is {2} grams total.".format(
            self.name, self.nutrition["carbs"], self.amount
        )


    def scaleAmount(self, n):
        """ Returns scaled amount and nutritional facts of ingredient by n"""
        pass

egg = ingredient("egg", {"fats": 5, "carbs": 7, "proteins": 14}, 35.0)
print(egg)
