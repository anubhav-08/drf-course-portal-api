from django.db.models.query import RawQuerySet
from django.http import request
from rest_framework import serializers
from cart.models import Cart
from re import I
from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from courses.models import Course
from .models import Cart
from .serializers import CartSerializer
# Create your views here.
class CartApiView(APIView):

    def get(self, request):
        cart = Cart.objects.get(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def post(self, request): #for adding course to cart
        slug = request.POST.get('slug') 
        course = Course.objects.get(slug = slug)
        cart = Cart.objects.get(user = request.user)
        cart.courses.add(course)
        cart.save()        
        return Response({"message" : "course added to cart successfully"})
    
    def delete(self, request): # for removing course from cart
        slug = request.POST.get('slug')
        course = Course.objects.get(slug = slug)
        cart = Cart.objects.get(user = request.user)
        cart.courses.remove(course)
        cart.save()        
        return Response({"message" : "course removed from cart successfully"})

# class AddToCart(APIView):

#     def post(self, request):
#         course = Course.objects.get(slug = slug)
#         cart = Cart.objects.get(user = request.user)
#         cart.courses.add(course)
#         serializer = CartSerializer(cart)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.error_messages)