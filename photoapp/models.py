from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profilepic = models.ImageField(upload_to = 'images')
    bio = models.CharField(max_length=100)
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Likes(models.Model):
    likes = models.IntegerField(default=0)

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=25)
    caption = models.CharField(max_length=150)
    profile = models.ForeignKey(Profile,  on_delete=models.CASCADE, default=None)
    likes = models.ForeignKey(Likes, on_delete=models.CASCADE, default=0)
    comment = models.CharField(max_length=150)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)