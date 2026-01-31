from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True,db_index=True)
    password = models.CharField(max_length=100)
    tenent=models.CharField(max_length=100,db_index=True)
    username=models.CharField(max_length=150,unique=True,db_index=True)
    storage_used=models.BigIntegerField(default=0)
    storage_limit=models.BigIntegerField(default=1073741824)

    def __str__(self):
        return self.name

