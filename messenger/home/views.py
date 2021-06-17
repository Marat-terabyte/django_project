from django.shortcuts import render
from django.http import HttpResponse
from . import models


def home_view(request):
	model = models.citata_model.objects.all()
	return render(request , 'home/index.html' , {'model':model})
