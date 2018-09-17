from django.urls import path
from chartGenerator import views



urlpatterns = [
	path('hw', views.indexHelloWorld),
	path('chart', views.displayChart),
	path('chartform', views.generateChart),
	path('', views.index),
]

