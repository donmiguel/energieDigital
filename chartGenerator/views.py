from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader

from chartGenerator.mobius import mobius
from chartGenerator.models import Parameter


def indexHelloWorld(request):
	return HttpResponse("Hello, world.")


def index(request):
	template = loader.get_template('index.html')

	return HttpResponse(template.render(None, request))



def displayChart(request):
	template = loader.get_template('chart.html')

	return HttpResponse(template.render(None, request))



class parameterForm(ModelForm):
	class Meta:
		model = Parameter
		fields = '__all__'


def generateChart(request):
	if request.method == "POST":
		form = parameterForm(request.POST)

		if form.is_valid():
			# generate chart
			parameter = form.save(commit=False)
			mobius(start=parameter.start, stop=parameter.stop, colored=parameter.colored,
			       numSamplesU=parameter.numSamplesU, numSamplesV=parameter.numSamplesU, path='chartGenerator/static/')
			parameter.save()
			return displayChart(request)
	else:
		form = parameterForm()

	return  render(request, 'chartform.html', {'form' : form})
