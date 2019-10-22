from django.db import models

# Create your models here.

class Student(models.Model):
    first_name= models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email =     models.CharField(max_length=40)
    Address=      models.CharField(max_length=50)
    class Meta:  
        db_table = "student"

