from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.

def topics(request):
    return render(request, 'forum/forum.html')

def show_topic(request, topic_id):
    pass

def UserLoginView(LoginView):
    template_name='login.html'