from django.db import models

# Create your models here.

class Parameter(models.Model):
	start = models.FloatField()
	stop = models.FloatField()

