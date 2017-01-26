from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse ("Rango says is the link -->    " + " " + "http://127.0.0.1:8000/django1/about")

from django.http import HttpResponse
def about(request):
    return HttpResponse("Rango says this is the about page")