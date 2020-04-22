from django.db import models

# Create your models here.


class Language(models.Model):
    name = models.CharField(primary_key= True, max_length=200)



class Projects(models.Model):
    name = models.CharField(max_length=200)
    datecreated = models.DateField()
    lastmodified = models.DateField()
    views = models.IntegerField(default=0)
    languages = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null= True)
    url = models.CharField(max_length=200)
    info = models.CharField(max_length=1000)
