from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olar fernando")

# Create your views here.
