from django.urls import path

from .views import *

urlpatterns = [
    path('', CartApiView.as_view(), name='cart'),
]
