from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, default='default.png', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
