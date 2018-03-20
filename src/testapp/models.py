from django.db import models

# Create your models here.
class Testapp(models.Model):
    surname = models.CharField(max_length=64)
    course = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
