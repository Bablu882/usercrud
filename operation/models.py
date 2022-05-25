
from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mobile=models.CharField(max_length=10)
    city=models.CharField(max_length=20)