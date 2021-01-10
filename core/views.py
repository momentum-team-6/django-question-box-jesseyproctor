from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("homepage")

def add_user(request):
    return HttpResponse("hi")

def user_login(request):
    return HttpResponse("k")

def user_page(request):
    return HttpResponse("p")
