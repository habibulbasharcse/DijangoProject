from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello Home page")

def contact(request) :
    return HttpResponse("<h1 style='color: red;'>Hello contact page</h1>")

def show_task(request) :
    return HttpResponse("this is show page")
def showTaskWithPara(request, id) :
    return HttpResponse(f"Showing task with parameter {id}")
def txt(request , id) :
    return HttpResponse(f"this is Txt And id is: {id}")