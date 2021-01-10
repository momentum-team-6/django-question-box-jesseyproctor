from django.shortcuts import render
from django.http import Httpresponse

# Create your views here.
def homepage(request):
    return Httpresponse("homepage")

def add_user(request):
    return Httpresponse("hi")

def user_login(request):
    return Httpresponse("k")

def user_page(request):
    return Httpresponse("p")
