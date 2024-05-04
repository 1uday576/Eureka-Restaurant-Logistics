from pickletools import read_uint1
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *

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

def cardInfo(request):
    Name = request.headers["Name"]
    meal = Meal.objects.filter(name=Name)[0]
    cost = meal.cost
    ingredientList = meal.ingredientList
    data = {"cost":cost, "list":ingredientList}
    
    return JsonResponse(data)