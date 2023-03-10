from django.contrib import admin
from .models import *
from category.models import Category

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'desc')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'desc')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
