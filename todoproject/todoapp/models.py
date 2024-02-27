from django.db import models

# Create your models here.

class Ttask(models.Model):
    name=models.CharField(max_length=250)
    priority=models.IntegerField()
    date=models.DateField()
