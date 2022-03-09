from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class Profile(models.Model):
    profilepic = models.ImageField(upload_to = 'images/')
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

class MyUser(AbstractBaseUser):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length= 50)
    username = models.CharField(max_length = 50, unique = True)
    email = models.EmailField(max_length=60, unique=True)
    phone_number = models.CharField(max_length = 50)
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True