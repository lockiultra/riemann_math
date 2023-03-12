from django.db import models
from category.models import Category
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class RiemannCourse(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='images/courses/')
    categories = models.ManyToManyField(Category)
    slug_name = models.SlugField(blank=True)
    course_menu = models.ForeignKey('CourseMenu', on_delete=models.PROTECT, null=True, blank=True)

class CourseMenu(MPTTModel):
    title = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['id']

class Course(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=False)
    link = models.URLField(blank=False)
    img = models.ImageField(upload_to='images/courses/')
    categories = models.ManyToManyField(Category)
    slug_name = models.SlugField(null=True)
    course_menu = models.ForeignKey('CourseMenu', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'
        ordering = ['title', 'id']

class Comment(models.Model):
    author = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey('Course', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.author}: {self.text}'
    
    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
        ordering = ['date', 'author']