from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def hola(request):
    return HttpResponse("<h1 style='text-align:center'>My App de Django</h1>")