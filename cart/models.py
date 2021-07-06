from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

from courses.models import Course

User = get_user_model()

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE, primary_key=True)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return (self.user.name + "'s cart")