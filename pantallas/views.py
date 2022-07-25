from urllib import request
from urllib.request import Request
from django.shortcuts import render
from pantallas.models import Persona, Mascota, SpaAnimal
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pantallas.forms import (PersonaFormulario, MascotaFormulario, 
SpaAnimalFormulario, PersonaBusqueda)
from django.urls import reverse, reverse_lazy

def mostrar_inicio(request):
    return render(request, "pantallas/inicio.html", {})

def mostrar_perfil(request):
    return render(request, "pantallas/perfil.html", {})

def mostrar_reserva(request):
    return render(request, "pantallas/reserva.html", {})

def personaFormulario(request):
    if request.method == "POST":
        pass
    else:
        miFormulario = PersonaFormulario()
        return render(request, "pantallas/personaFormulario.html",{"miFormulario":miFormulario})

def formulario_busqueda_persona(request):
    busqueda_formulario = PersonaBusqueda()

    if request.GET:
        personas = Persona.objects.filter(nombre= busqueda_formulario['criterio']).all()
        return render(request, "pantallas/personabusqueda.html", {"personas": personas})

    return render(request, "pantallas/personabusqueda.html",{"busqueda_formulario":busqueda_formulario})


class MascotaCreateView(CreateView):
    model = Mascota
    template_name = "pantallas/mascota_formulario.html"
    fields = "__all__"   

    def get_success_url(self) -> str:
         return reverse_lazy('pantallas:base')

class PersonaCreateView(CreateView):
    model = Persona
    template_name = "pantallas/persona_formulario.html"
    fields = "__all__"   

    def get_success_url(self) -> str:
         return reverse_lazy('pantallas:base')