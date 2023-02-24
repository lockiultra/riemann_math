from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('books/', books, name='books'),
    path('books/topic/<slug:topic_name>/', books_topic, name='topic'),
    path('books/post/<slug:post_name>/', post, name='post')
]
