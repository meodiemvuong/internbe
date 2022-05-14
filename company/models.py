from django.db import models

# Create your models here.


    


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=2000)
    

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Level(models.Model):
    level = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

