from django.db import models

class empresa1(models.Model):
    title = models.CharField(max_length=80)
    age = models.IntegerField()

    def __str__(self):
        return self.title
    
class empresa2(models.Model):
    title = models.CharField(max_length=80)
    age = models.IntegerField()

    def __str__(self):
        return self.title

class empresa3(models.Model):
    title = models.CharField(max_length=80)
    age = models.IntegerField()

    def __str__(self):
        return self.title

# Create your models here.
