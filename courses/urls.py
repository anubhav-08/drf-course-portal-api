from django.urls import path
from .views import *

urlpatterns = [
    path('', CourseApiView.as_view(), name='courses'),
]
