from urllib import request
from urllib.request import Request
from django.shortcuts import render
from pantallas.models import Persona, Mascota, SpaAnimal
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pantallas.forms import (PersonaFormulario, MascotaFormulario, 
SpaAnimalFormulario, PersonaBusqueda )
from django.urls import reverse, reverse_lazy


def mostrar_index(request):
    return render(request, "pantallas/inicio.html", {})

def mostrar_inicio(request):
    return render(request, "pantallas/inicio.html", {})

def mostrar_reserva(request):
    return render(request, "pantallas/reserva_form.html", {})

def formulario_busqueda_persona(request):

    busqueda_formulario = PersonaBusqueda()

    if request.GET:
        busqueda_formulario = PersonaBusqueda(request.GET)
        if busqueda_formulario.is_valid():
            personas = Persona.objects.filter(nombre=busqueda_formulario.cleaned_data.get("criterio")).all()
            return render(request, "pantallas/persona_busqueda.html", {"busqueda_formulario":busqueda_formulario, "personas":personas})

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
    template_name = "pantallas/reserva_form.html"
    fields = "__all__"   

    def get_success_url(self) -> str:
         return reverse_lazy('pantallas:inicio')

def reserva_formulario(request):
    if request.method == 'POST':
        reservaFormulario = SpaAnimalFormulario(request.POST)
        print (reservaFormulario)
        if reservaFormulario.is_valid:
            informacion = reservaFormulario.cleaned_data
            reserva = SpaAnimal(nombre=informacion['nombre'], reserva=informacion['reserva'], pago=informacion['pago'])
            reserva.save()
            return render(request, "pantallas/reserva_form.html")
    else:
        reservaFormulario= SpaAnimalFormulario()
    return render(request, "pantallas/reserva_form.html", {"reservaFormulario":reservaFormulario})