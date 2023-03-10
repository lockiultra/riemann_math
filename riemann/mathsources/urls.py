from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='home'),
    path('books/', books, name='books'),
    path('books/topic/', books_topic, name='books_all'),
    path('books/topic/<slug:topic_name>/', books_topic, name='books_topic'),
    path('books/post/<slug:book_name>/', post, name='post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)