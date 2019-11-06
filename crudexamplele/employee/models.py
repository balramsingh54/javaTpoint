from django.db import models

# Create your models here.

class Employee(models.Model):
    eId = models.CharField(max_length=20)
    eName = models.CharField(max_length=20)
    eEmail = models.CharField(max_length=20)
    eContact = models.CharField(max_length=20)

    class Meta:  
       db_table = "employee"