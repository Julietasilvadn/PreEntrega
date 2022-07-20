from django.shortcuts import render
from pantallas.models import Persona, Mascota, SpaAnimal
from pantallas.forms import (PersonaFormulario, MascotaFormulario, 
SpaAnimalFormulario, PersonaBusqueda)

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