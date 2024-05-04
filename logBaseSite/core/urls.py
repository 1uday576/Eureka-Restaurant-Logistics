from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name="landing"),
    #path to the stock named 'stock'
    path("stock", views.stock, name="stock")
]