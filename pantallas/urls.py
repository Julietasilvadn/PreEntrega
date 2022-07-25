from django.contrib import admin
from django.urls import path, include
from pantallas.views import *

pantallas_patterns =( [
    path('', mostrar_inicio, name='inicio'),
    path('perfil/', mostrar_perfil, name= 'perfil'),
    path('reserva/', mostrar_reserva, name='reserva'),
    path('formulario/persona/', personaFormulario, name='persona'),
    path('buscar/personas/', formulario_busqueda_persona, name='busqueda'),
    path('create/', MascotaCreateView.as_view(), name='create'),
    path('create_person/', PersonaCreateView.as_view(), name='crear_persona'),    
],'pantallas' )