from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    cpf = models.CharField(max_length=255, unique=True)
    gr = models.CharField(max_length=255, unique=True)
    birth_date = models.DateField()
    telephone =  models.IntegerField()
    cep = models.CharField(max_length=255)
    residential_num = models.IntegerField()
    residential_complement = models.CharField(max_length=255, null=True)
    is_apartment = models.BooleanField(default=False)
    