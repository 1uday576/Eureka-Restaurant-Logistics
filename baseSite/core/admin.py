from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Meal)
admin.site.register(TransactionIngredient)
admin.site.register(TransactionMeal)