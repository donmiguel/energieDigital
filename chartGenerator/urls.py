from django.urls import path
from chartGenerator import views



urlpatterns = [
	path('', views.indexHelloWorld),
]

