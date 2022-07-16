from django.contrib import admin
from django.urls import path
from app_entrega.views import (saludo, mostrar_index)

urlpatterns = [
    path('mi-pagina/', mostrar_index),
]