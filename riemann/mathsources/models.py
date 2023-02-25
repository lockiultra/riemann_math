from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    authors = models.ManyToManyField('Author')
    categories = models.ManyToManyField('Category')
    links = models.ForeignKey('Links', on_delete=models.PROTECT)
    img = models.ImageField(upload_to='images/')
    time_create = models.DateTimeField(auto_now=True)
    time_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'
        ordering = ['time_create', 'title']

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Авторы'
        verbose_name_plural = 'Авторы'
        ordering = ['name']

class Category(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']

class Links(models.Model):
    ozon_link = models.CharField(max_length=255, blank=True)
    ymarket_link = models.CharField(max_length=255, blank=True)
    wb_link = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Ссылки'
        verbose_name_plural = 'Ссылки'
