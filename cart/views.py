from rest_framework.views import APIView
from rest_framework.response import Response

from courses.models import Course
from .models import Cart
from .serializers import CartSerializer

# Create your views here.
class CartApiView(APIView):

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
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
