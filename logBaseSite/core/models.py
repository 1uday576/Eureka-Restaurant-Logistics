from django.db import models

ING_CATEGORY = {
    "Fruit": "Fruit",
    "Vegetable":"Vegetabl",
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
class Ingredients(models.Model):
    name = models.CharField(max_length=200)
    typeCategory = models.CharField(max_length=50, choices=ING_CATEGORY)
    stock = models.IntegerField()

class Meals(models.Model):
    name = models.CharField(max_length=200)
    ingredientList = models.JSONField()
    typeCategory = models.CharField(max_length=50,choices=MEAL_CATEGORY)
    cost = models.DecimalField(max_digits=2, decimal_places=2)

class TransactionMeals(models.Model):
    meal = models.ForeignKey(Meals, on_delete=models.CASCADE)
    date = models.DateTimeField("date bought")
    numberSold = models.IntegerField()

class TransactionIngredients(models.Model):
    ingredient =  models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    date = models.DateTimeField("date bought")
    numberSold = models.IntegerField()