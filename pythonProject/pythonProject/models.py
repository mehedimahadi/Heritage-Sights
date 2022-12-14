from django.db import models
from django.contrib.auth.models import User
# from PIL import Image


class SignUp(models.Model):
    User_id = models.AutoField
    FullName = models.CharField(max_length=100)
    UserName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


class Signin(models.Model):
    User_id = models.AutoField
    UserName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


class Contact(models.Model):
    User_id = models.AutoField
    UserName = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Message = models.TextField()


class UserProfile(models.Model):
    GENRE_CHOICES = (
        ('Male', 'MALE'),
        ('Female', 'FEMALE'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    full_name = models.CharField(max_length=50)
    # Email = models.CharField(max_length=100)
    image = models.ImageField()
