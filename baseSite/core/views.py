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

def listStock(request):
    ingredient = Ingredient.objects.all()

    names = []
    amount = []
    for i in range(0, len(ingredient)):
        names.append(ingredient[i].name)
        amount.append(ingredient[i].stock)

    data = {'names':names, 'amount': amount}
    return JsonResponse(data)

def listOrder(request):
    listModel = TransactionMeal.objects.all()

    names = []
    amount = []
    for i in range(0, len(listModel)):
        names.append(listModel[i].meal)
        amount.append(listModel[i].numberSold)

    data = {'names':names, 'amount': amount}
    return JsonResponse(data)

def cardInfo(request):
    Name = request.GET.get("Name", "")
    meal = Meal.objects.filter(name=Name).first()
    if meal:
        cost = meal.cost
        ingredientList = meal.ingredientList
        data = {"cost": cost, "list": ingredientList}
    else:
        data = {"error": "Meal not found"}
    
    return JsonResponse(data)