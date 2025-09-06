from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_user(request) :
    return HttpResponse("hello users")

def showUserId(request, id):
    return HttpResponse(f"User Id is {id}")

