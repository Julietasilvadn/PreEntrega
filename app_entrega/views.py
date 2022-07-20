from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from app_entrega.models import Persona, Mascota, SpaAnimal

def mostrar_index(request):
    return render(request, 'app_entrega\index.html', {})

