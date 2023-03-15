from django.db import models
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.title
    
class Message(models.Model):
    content = models.TextField()
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

