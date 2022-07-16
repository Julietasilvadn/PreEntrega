from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=100)

class Mascota(models.Model):
    nombre=models.CharField(max_length=40)
    dueño=models.CharField(max_length=60)
    tipoDeAnimal=models.CharField(max_length=40)

class SpaAnimal(models.Model):
    nombre=models.CharField(max_length=60)
    reserva=models.DateField()
    pago=models.BooleanField()
