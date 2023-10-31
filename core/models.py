from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Department(models.Model):
    name= models.CharField(max_length=64)
    
    class Meta:
        ordering =('name',)
        verbose_name_plural= 'Departments'
        
    def __str__(self):
        return f"{self.name}"
    

