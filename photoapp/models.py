from django.db import models

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=25)
    caption = models.CharField(max_length=150)
    profile = models.ForeignKey( on_delete=models.CASCADE, default=None)
    likes = models.ForeignKey( on_delete=CASCADE, default=0)
    comment = models.CharField(max_length=150)