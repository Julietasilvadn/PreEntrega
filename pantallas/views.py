from django.shortcuts import render

def mostrar_inicio(request):
    return render(request, "pantallas/inicio.html", {})

def mostrar_perfil(request):
    return render(request, "pantallas/perfil.html", {})

def mostrar_reserva(request):
    return render(request, "pantallas/reserva.html", {})