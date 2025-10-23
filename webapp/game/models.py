from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    real_name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    challenges = models.ManyToManyField('Challenges', blank=True)

class Challenges(models.Model):
    name = models.CharField(max_length=200)
    rating = models.CharField(max_length=50)
    in_pool = models.BooleanField(default=True)