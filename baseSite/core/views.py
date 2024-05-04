from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def homePage(request):
    return render(request, 'index.html')

def stock(request):
    return HttpResponse("Works")

def cardInfo(request):
    Name = request.headers["Name"]
    meal = Meal.objects.filter(name=Name)[0]
    cost = meal.cost
    ingredientList = meal.ingredientList
    data = {"cost":cost, "list":ingredientList}
    
    return JsonResponse(data)