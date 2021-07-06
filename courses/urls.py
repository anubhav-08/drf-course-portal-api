from django.urls import path
from .views import *

urlpatterns = [
    path('', CourseApiView.as_view(), name='courses'),
    path('register/', RegisCourseApiView.as_view(), name='course-add'),
    path('checkout/', CheckoutApiView.as_view(), name='courses-checkout'),
    # path('registerd/',   )
]
