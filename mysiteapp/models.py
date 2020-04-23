from django.db import models
from datetime import datetime

# Create your models here.




class Projects(models.Model):
    projid = models.IntegerField(primary_key=True, default=1)
    name = models.CharField(max_length=200)
    datecreated = models.DateTimeField(default=datetime.now)
    lastmodified = models.DateTimeField(default=datetime.now)
    views = models.IntegerField(default=0)
    url = models.CharField(max_length=200)
    info = models.CharField(max_length=1000)
    mainlanguage = models.CharField(max_length=200)


class Language(models.Model):
    name = models.CharField(primary_key= True, max_length=200)
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE)
