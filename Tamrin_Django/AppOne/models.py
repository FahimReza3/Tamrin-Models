from django.db import models

# Create your models here.

class User(models.Model):
    id=models.IntegerField(primary_key=True , unique=True)
    Name=models.CharField(max_length=50)
    Family=models.CharField(max_length=50)
    Email=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
