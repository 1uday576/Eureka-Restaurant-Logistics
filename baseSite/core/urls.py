from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name="landing"),
    #path to the stock named 'stock'
    path("stock", views.stock, name="stock"),
    path("mealsNames", views.listMeals, name="mealsNames"),
    path("ingredientStock", views.listStock, name="ingredientStock"),
    path("cardInfo", views.cardInfo, name="cardInfo")
]