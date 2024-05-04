from django.db import models

# Create your models here.
from django.db import models

ING_CATEGORY = {
    "Bread":"Bread",
    "Fruit": "Fruit",
    "Vegetable":"Vegetable",
    "Meat": "Meat",
    "SeaFood": "Sea Food",
    "Poultery": "Poultery"
}

MEAL_CATEGORY = {
    "Beverages": "Beverages",
    "Sandwiches": "Sandwiches",
    "Burger": "Burger",
    "Soups": "Soups",
    "MainEntres": "Main Entres",
    "Dessert": "Dessert"
}

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    typeCategory = models.CharField(max_length=50, choices=ING_CATEGORY)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=200)
    ingredientList = models.JSONField()
    typeCategory = models.CharField(max_length=50,choices=MEAL_CATEGORY)
    cost = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

class TransactionMeal(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    date = models.DateTimeField("date bought")
    numberSold = models.IntegerField()

    def __str__(self):
        return self.meal

class TransactionIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    date = models.DateTimeField("date bought")
    numberSold = models.IntegerField()

    def __str__(self):
        return self.ingredient