from django.shortcuts import render
from category.utils.categories import get_categories
from courses.utils.course import get_course
from courses.utils.paginator import get_page_obj

# Create your views here.

def courses(request):
    return render(request, 'courses/courses.html', {'categories': get_categories()})

def add_comment(request):
    return render(request, 'courses/add_comment.html')

def courses_topic(request, cat_name):
    page_obj = get_page_obj(request, cat_name)
    return render(request, 'courses/courses_page.html', {'page_obj': page_obj})

def course_post(request, slug_name):
    course = get_course(slug_name)
    return render(request, 'courses/course_post.html', {'course': course})