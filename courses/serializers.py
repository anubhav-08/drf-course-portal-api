from django.db.models import fields
from rest_framework import serializers

from .models import Course, RegisteredCourses


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

class RegisteredCoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegisteredCourses
        fields = ['user', 'courses']