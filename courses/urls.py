from os import name
from django.urls import path
from .views import *

urlpatterns = [
    path('courses/', CourseApiView.as_view(), name='courses'),
]
