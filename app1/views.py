from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def vista1(request):
    return HttpResponse("<h1>Bienvenido a la Vista 1</h1>")

def vista2(request):
    return HttpResponse("<p>Esta es la Vista 2</p>")