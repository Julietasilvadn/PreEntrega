from django.contrib import admin
from django.urls import path, include
from pantallas.views import (mostrar_inicio, mostrar_perfil, 
mostrar_reserva, personaFormulario, formulario_busqueda_persona)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_entrega.urls')),
    path('inicio/', mostrar_inicio),
    path('perfil/', mostrar_perfil),
    path('reserva/', mostrar_reserva),
    path('formulario/persona/', personaFormulario),
    path('buscar/personas/', formulario_busqueda_persona)
]
