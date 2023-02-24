from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mathsources/index.html')

def books(request):
    pass

def books_topic(request):
    pass

def post(request):
    pass
