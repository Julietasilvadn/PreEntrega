from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from app_entrega.models import Persona, Mascota, SpaAnimal

def mostrar_index(request):
    return render(request, 'app_entrega\index.html', {})

def saludo(request):
    return HttpResponse("Hola, ¿Cómo estas?")

#Con esto muestro lo que guardo en la base de datos
#def mostrar_nombre(request):
#    context = {}
#    if request.GET:
#        context["nombre"] =request.GET["nombre"]
#    return render(request,"app_entrega/index.html", context)

