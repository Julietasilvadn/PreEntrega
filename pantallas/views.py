from urllib import request
from urllib.request import Request
from django.shortcuts import render
from pantallas.models import Persona, Mascota, SpaAnimal
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pantallas.forms import (PersonaFormulario, MascotaFormulario, 
SpaAnimalFormulario, PersonaBusqueda)
from django.urls import reverse, reverse_lazy


def mostrar_index(request):
    return render(request, "pantallas/inicio.html", {})

def mostrar_inicio(request):
    return render(request, "pantallas/inicio.html", {})

def mostrar_reserva(request):
    return render(request, "pantallas/reserva.html", {})

def formulario_busqueda_persona(request):
    busqueda_formulario = PersonaBusqueda()

    if request.GET:
        personas = Persona.objects.filter(nombre= busqueda_formulario).all()
        return render(request, "pantallas/persona_busqueda.html", {"personas": personas})

    return render(request, "pantallas/persona_busqueda.html",{"busqueda_formulario":busqueda_formulario})

class MascotaCreateView(CreateView):
    model = Mascota
    template_name = "pantallas/mascota_form.html"
    fields = "__all__"   

    def get_success_url(self) -> str:
         return reverse_lazy('pantallas:inicio')

class PersonaCreateView(CreateView):
    model = Persona
    template_name = "pantallas/persona_form.html"
    fields = "__all__"   

    def get_success_url(self) -> str:
         return reverse_lazy('pantallas:inicio')

class ReservaCreateView(CreateView):
    model = SpaAnimal
    template_name = "pantallas/reserva.html"
    fields = "__all__"   

    def get_success_url(self) -> str:
         return reverse_lazy('pantallas:inicio')

