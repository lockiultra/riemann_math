from django.db import models
from category.models import Category

# Create your models here.

# class RiemannCourse(models.Model):
#     pass

class Course(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=False)
    link = models.URLField(blank=False)
    img = models.ImageField(upload_to='images/courses/')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'
        ordering = ['title', 'id']