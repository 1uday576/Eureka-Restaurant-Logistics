from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'index.html')

def stock(request):
    return HttpResponse("Works")