from django.contrib import admin
from .models import Course, RegisteredCourses
# Register your models here.

admin.site.register(Course)
admin.site.register(RegisteredCourses)
