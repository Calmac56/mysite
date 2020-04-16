from django.db import models

# Create your models here.

class projects(models.Model):
    name = models.CharField(max_length=200)
    datecreated = models.DateField()
    lastmodified = models.DateField()
    views = models.IntegerField(default=0)
