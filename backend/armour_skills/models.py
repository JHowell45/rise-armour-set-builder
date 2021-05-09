from django.db import models

# Create your models here.
class ArmourSkill(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    level = models.IntegerField()