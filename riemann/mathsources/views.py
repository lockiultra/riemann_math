from django.shortcuts import render
from django.http import HttpResponse
from .utils.categories import get_categories
from .utils.paginator import get_page_obj
from .utils.post import get_book_post

# Create your views here.

def index(request):
    return render(request, 'mathsources/index.html')

def books(request):
    return render(request, 'mathsources/books.html', {'categories': get_categories()})

def books_topic(request, topic_name=''):
    page_obj = get_page_obj(request, topic_name)
    print(page_obj)
    return render(request, 'mathsources/books_page.html', {'page_obj': page_obj, 'topic_name': topic_name})

def post(request, book_name):
    book = get_book_post(book_name)
    return render(request, 'mathsources/books_post.html', {'book': book})