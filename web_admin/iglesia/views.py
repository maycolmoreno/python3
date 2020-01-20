from django.shortcuts import render
from .models import *
# Create your views here.


def mostrar_inicio(request):
	return render(request, 'backend/index.html', {})
