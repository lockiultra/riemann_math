from django.urls import path
from .views import *

urlpatterns = [
    path('', courses, name='courses'),
    path('add_comment/', add_comment, name='add_comment'),
]