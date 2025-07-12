from django.shortcuts import render
from django.http import HttpRequest

def hello_world(request):
    return HttpRequest("Hello World!")

# Create your views here.
