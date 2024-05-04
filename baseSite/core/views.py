import datetime
from pickletools import read_uint1
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
import json

# Create your views here.
def homePage(request):
    return render(request, 'index.html')

def stock(request):
    return render(request, 'Stock.html')

def listMeals(request):
    meals = Meal.objects.all()

    names = []
    for i in range(0, len(meals)):
        names.append(meals[i].name)

    data = {'names':names}

    # print(data)
    # response = HttpResponse()
    # response.headers['DataTest'] = data
    # return response

    return JsonResponse(data)

def listIngredient(request):
    ingredient = Ingredient.objects.all()

    names = []
    for i in range(0, len(ingredient)):
        names.append(ingredient[i].name)

    data = {'names':names}

def cardInfo(request):
    Name = request.headers["Name"]
    meal = Meal.objects.filter(name=Name)[0]
    cost = meal.cost
    ingredientList = meal.ingredientList
    data = {"cost":cost, "list":ingredientList}
    
    return JsonResponse(data)

def postMeal(request):
    mealList = json.load(request.headers["List"])["meals"]

    for key, value in mealList.items():
        t = TransactionMeal(meal = key, date = datetime.date.today(), numberSold=value)
        t.save()

        inList = meal.ingredientList
        for ing, amount in inList.items():
            tI = TransactionIngredient(ingredient = ing, date = datetime.date.today(), numberSold =amount)
            tI.save()
