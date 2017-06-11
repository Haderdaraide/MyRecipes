from django.db import models

food_types = (('snack', 'Snack'), ('dinner', 'Dinner'), ('breakfast', 'Breakfast'), ('lunch', 'Lunch'))

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=30)
    recipe_description = models.CharField(max_length=300)
    recipe_type = models.CharField(max_length=10, choices=food_types)

    def __str__(self):
        return self.recipe_name

#class Ingredients(models.Model):



