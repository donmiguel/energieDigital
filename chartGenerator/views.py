import numpy as np
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime as dt
import matplotlib.pyplot as plt

# Create your views here.
from django.template import loader

from chartGenerator.mobius import mobius
from chartGenerator.models import Parameter


# Hello world view
def indexHelloWorld(request):
	return HttpResponse("Hello, world.")

# example view using a html template
def index(request):
	template = loader.get_template('index.html')

	return HttpResponse(template.render(None, request))


# view which displays an image
def displayChart(request):
	# use the template where we want to display the generated image
	template = loader.get_template('chart.html')

	return HttpResponse(template.render(None, request))


# form to get the input data (parameters) for the calculations
class parameterForm(ModelForm):
	class Meta:
		model = Parameter
		fields = '__all__'

# main view for mobius generation
def generateChart(request):
	if request.method == "POST":
		form = parameterForm(request.POST)

		if form.is_valid():
			# generate chart
			parameter = form.save(commit=False)
			mobius(start=parameter.start, stop=parameter.stop, colored=parameter.colored,
			       numSamplesU=parameter.numSamplesU, numSamplesV=parameter.numSamplesU, path='chartGenerator/static/')
			parameter.save()

			#redirect to chart display view
			return displayChart(request)
	else:
		form = parameterForm()

	return  render(request, 'chartform.html', {'form' : form})
