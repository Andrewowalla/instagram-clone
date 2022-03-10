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

    def __str__(self):
        return str(self.likes)

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=25)
    caption = models.CharField(max_length=150)
    profile = models.ForeignKey(Profile,  on_delete=models.CASCADE, default=None)
    likes = models.ForeignKey(Likes, on_delete=models.CASCADE, default=0)
    # comment = models.CharField(max_length=150)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

class Comment(models.Model):
    comment = models.TextField()
    upload_time = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.image

class MyUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, username, password=None):
        if not email:
            raise ValueError("Email is required")

        if not username:
            raise ValueError("User must have a username")

        user= self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = self.normalize_email(email),
            password = password
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True

        user.save(using = self._db)
        
        return user

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

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True