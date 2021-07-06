from django.shortcuts import render, HttpResponse
from rest_framework import generics, mixins

from .models import Course
from .serializers import CourseSerializer
# Create your views here.

class CourseApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        return self.list(request)


# class BuyCourseApiView(generics.GenericAPIView):

#     def post(self, request, pk):
