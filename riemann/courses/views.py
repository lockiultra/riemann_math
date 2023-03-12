from django.shortcuts import render
from category.utils.categories import get_categories

# Create your views here.

def courses(request):
    return render(request, 'courses/courses.html', {'categories': get_categories()})