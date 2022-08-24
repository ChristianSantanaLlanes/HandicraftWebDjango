from django.db import models
from user.models import User
from app.models import Product

# Create your models here.

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    productos = models.ManyToManyField(Product, related_name='productos')
    
    def __str__(self):
        return self.user.email