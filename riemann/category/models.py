from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to='images/categories', null=True)
    slug_name = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']