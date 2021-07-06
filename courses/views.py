from django.contrib.auth.decorators import login_required
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from cart.models import Cart
from .models import Course, RegisteredCourses
from .serializers import CourseSerializer
# Create your views here.

class CourseApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        return self.list(request)


class CheckoutApiView(APIView):
    
    def post(self, request):
        cart = Cart.objects.get(user = request.user)
        cart_courses = cart.courses.all()
        regis_courses, _ = RegisteredCourses.objects.get_or_create(user = request.user)
        for course in cart_courses:
            regis_courses.courses.add(course)
            cart.courses.remove(course)
        regis_courses.save()
        cart.save()
        
        return Response({"message" : "all courses registered successfully"})

class RegisCourseApiView(mixins.ListModelMixin, generics.GenericAPIView):
    
    def get_queryset(self):
        registered_courses = RegisteredCourses.objects.get(user = self.request.user)
        courses = registered_courses.courses.all()
        return courses
    
    serializer_class = CourseSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        slug = request.POST.get('slug')
        course = Course.objects.get(slug = slug)
        regis_courses, _ = RegisteredCourses.objects.get_or_create(user = request.user)
        regis_courses.courses.add(course)
        regis_courses.save()

        return Response({"message" : "Course Registered Successfully"})