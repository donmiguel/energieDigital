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


def exampleView(request):
	dataSource = 'chartGenerator/daq/example.csv'

	# Datenimport
	data = np.loadtxt(dataSource, dtype='f', delimiter=';', skiprows=1, usecols=[1, 2, 3, 4, 10])
	hGlo = data[:, 0]  # [W/m2]
	hDif = data[:, 1]  # [W/m2]
	tAmb = data[:, 2]  # [W/m2]
	pLoad = data[:, 3]  # [W] Verbrauchsprofil
	zapf = data[:, 4]  # [l/15min] Profil für Warmwasserbezug

	tutcIn = np.loadtxt(dataSource, dtype='U', delimiter=';', skiprows=1, usecols=[0])
	tutc = []  # leere Liste
	for t in range(tutcIn.size):
		tutc.append(dt.datetime.strptime(tutcIn[t], '%Y-%m-%d %H:%M:%S'))
	tutc = np.array(tutc)  # umwandeln in ein numpy Array

	lfStd = np.zeros(tutc.size)
	for t in range(tutc.size):
		# berechnet laufender Tag im Jahr
		noDay = (tutc[t] - dt.datetime(tutc[0].year, 1, 1, 0)).days
		# [h] berechnet laufende Stunde im Tag
		noHou = tutc[t].hour + (tutc[t].minute) / 60.0 + (tutc[t].second) / 3600.0
		lfStd[t] = noDay * 24 + noHou

	deltaT = lfStd[1] - lfStd[0]  # [h]

	hDir = hGlo - hDif

	hDir[hDir < 0] = 0  # wichtig
	hDif[hDif < 0] = 0  # wichtig
	hGlo[hGlo < 0] = 0  # wichtig

	a = int(0)  # Anfangstag
	e = int(7 * 24 / deltaT)  # Endtag

	plt.figure(3, figsize=(8,4))# Grösse des Plots (figsize) in Zoll
	plt.plot_date(tutc[a:e], hGlo[a:e], 'g', label='Globalstrahlung')
	plt.plot_date(tutc[a:e], hDir[a:e], 'r', label='Direktstrahlung')
	plt.plot_date(tutc[a:e], hDif[a:e], 'b', label='Diffusstrahlung')
	plt.xlabel('Zeit [h]');
	plt.ylabel('Strahlung [W/m2]');
	plt.legend(loc="upper left")

	plt.savefig('chartGenerator/static/chart.png', bbox_inches="tight")

	# call chart display view with chart template
	return displayChart(request)