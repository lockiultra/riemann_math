from django.shortcuts import render
from .utils.categories import get_categories

# Create your views here.

def index(request):
    return render(request, 'mathsources/index.html')

def books(request):
    return render(request, 'mathsources/books.html', {'categories': get_categories()})

def books_topic(request):
    pass

def post(request):
    pass