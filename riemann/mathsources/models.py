from django.db import models
from category.models import Category

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    authors = models.ManyToManyField('Author')
    categories = models.ManyToManyField(Category)
    img = models.ImageField(upload_to='images/')
    time_create = models.DateTimeField(auto_now=True)
    time_update = models.DateTimeField(auto_now_add=True)
    link = models.JSONField(default=dict, null=True)
    slug_name = models.SlugField(null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'
        ordering = ['time_create', 'title']

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Авторы'
        verbose_name_plural = 'Авторы'
        ordering = ['name']