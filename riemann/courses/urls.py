from django.urls import path
from .views import *

urlpatterns = [
    path('', courses, name='courses'),
    path('add_comment/<slug:slug_name>', add_comment, name='add_comment'),
    path('topic/<slug:cat_name>/', courses_topic, name='courses_page'),
    path('post/<slug:slug_name>', course_post, name='course_post'),
]