from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.



class Product(models.Model):
    
    Type = models.CharField(max_length=100, null= True)
    Material = models.CharField(max_length=100, null= True)
    Cost = models.IntegerField(null = True)
    Design = models.CharField(max_length=100, null= True)
    Image = models.ImageField(upload_to="product", height_field=None, width_field=None, max_length=100)


class MainProduct(models.Model):
    
    Type = models.CharField(max_length=100, null= True)
    Material = models.CharField(max_length=100, null= True)
    Cost = models.IntegerField(null = True)
    Design = models.CharField(max_length=100, null= True)
    Image = models.ImageField(upload_to="mproduct", height_field=None, width_field=None, max_length=100)