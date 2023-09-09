# from django.contrib.auth.models import User
from dbpost.models.core_models import BaseTimeStampModel
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.

User = get_user_model()

class PostCategory(BaseTimeStampModel):
    CATEGORY_NAME_OPTIONS = (
        ('Category_one', 'Category 01'),
        ('category_two', 'Category 02'),
        ('category_three', 'Category 03'),
    )
    name = models.CharField(max_length=14, choices=CATEGORY_NAME_OPTIONS)
    value = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
class Post(BaseTimeStampModel):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to="assets/post_images/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.DateTimeField(timezone.now)
    updated = models.DateTimeField(timezone.now)
    category = models.ManyToManyField(PostCategory, related_name='posts')

