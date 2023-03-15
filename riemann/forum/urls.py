from django.urls import path
from django.contrib.auth.views import LoginView
from forum.views import *

urlpatterns = [
    path('', topics, name='forum'),
    path('topic/<slug:topic_title>/', show_topic, name='show_topic'),
    path('login/', LoginView.as_view(), name='login'),
]