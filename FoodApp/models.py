from django.db import models
from django.contrib.auth .models import User

# Create your models here.

class food (models.Model):
    name=models.CharField(max_length=30)
    carbs=models.FloatField()
    protein=models.FloatField()
    facts=models.FloatField()
    calories=models.FloatField()
    calcium=models.FloatField
    
    def __str__(self):
        return self.name