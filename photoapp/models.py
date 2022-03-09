from django.db import models

# Create your models here.

class Profile(models.Model):
    profilepic = models.ImageField(upload_to = 'image')
    bio = models.CharField(max_length=100)
    username = models.CharField(max_length=20)

class Likes(models.Model):
    likes = models.IntegerField(default=0)

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=25)
    caption = models.CharField(max_length=150)
    profile = models.ForeignKey(Profile,  on_delete=models.CASCADE, default=None)
    likes = models.ForeignKey(Likes, on_delete=models.CASCADE, default=0)
    comment = models.CharField(max_length=150)