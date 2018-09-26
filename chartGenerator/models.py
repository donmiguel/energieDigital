from django.db import models

# Create your models here.

class Parameter(models.Model):
	start = models.FloatField('Start')
	stop = models.FloatField('Stop')
	numSamplesU = models.FloatField('numSamplesU', default=50)
	numSamplesV = models.FloatField('numSamplesV', default=10)
	colored = models.BooleanField('Colored', default=True)
