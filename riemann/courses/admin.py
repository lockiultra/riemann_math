from django.contrib import admin
from .models import Course, Comment

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'desc')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'date')
    list_display_links = ('id',)
    search_fields = ('author',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Comment, CommentAdmin)