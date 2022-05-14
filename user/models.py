from django.db import models

from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from company.models import Level, Company, Employee

# Create your models here.



class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_company(self):
        return self.company
