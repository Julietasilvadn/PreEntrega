from django.contrib import admin
from django.urls import path, include
from pantallas.views import *

pantallas_patterns =( [
    path('', mostrar_inicio, name='inicio'),
    path('reserva/', mostrar_reserva, name='reserva'),
    path('buscar/personas/', formulario_busqueda_persona, name='busqueda'),
    path('create/', MascotaCreateView.as_view(), name='create'),
    path('create/person/', PersonaCreateView.as_view(), name='crear_persona'), 
    path('create/reserva/', ReservaCreateView.as_view(), name='crear_reserva'),
    
      
],'pantallas' )