from django.contrib import admin
from .models import Course, RegisteredCourse
# Register your models here.

admin.site.register(Course)
admin.site.register(RegisteredCourse)
