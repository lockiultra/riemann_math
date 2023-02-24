from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mathsources/index.html')

def books(request):
    return render(request, 'mathsources/books.html')

def books_topic(request):
    pass

def post(request):
    pass
