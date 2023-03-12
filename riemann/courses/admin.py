from django.contrib import admin
from .models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'desc')

admin.site.register(Course, CourseAdmin)