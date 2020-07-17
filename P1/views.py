from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello World")#HttpResponse(HTML tag as an argument)

def home(request):
    return HttpResponse("<h1>Welcome to Homepage<h1>")

def html_demo1(request):
    return render(request,"Sample.html")

def html_demo2(request):
    return render(request,"sample_2.html")