from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from chartGenerator.mobius import mobius


def indexHelloWorld(request):
	return HttpResponse("Hello, world.")


def index(request):
	template = loader.get_template('index.html')

	return HttpResponse(template.render(None, request))



def generateChart(request):
	template = loader.get_template('chart.html')

	# generate chart
	mobius()

	return HttpResponse(template.render(None, request))