from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")#HttpResponse(HTML tag as an argument)

def home(request):
    return HttpResponse("Welcoem to Homepage")
