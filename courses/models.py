from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, primary_key=True, auto_created=False)
    short_description = models.TextField(blank=False, max_length=60)
    description = models.TextField(blank=False)
    outcome = models.CharField(max_length=400)
    prerequisite = models.CharField(max_length=400)
    language = models.CharField(max_length=200)
    price = models.IntegerField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)

class RegisteredCourses(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='registered')
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return (self.user.username + "'s courses")