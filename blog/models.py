from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class  Record(models.Model):
    name=models.CharField(max_length=200,primary_key=True)
    id=models.IntegerField()
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state= models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)