from django.db import models

class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Mascota(models.Model):
    nombre=models.CharField(max_length=40)
    dueño=models.CharField(max_length=60)
    tipoDeAnimal=models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

class SpaAnimal(models.Model):
    nombre=models.CharField(max_length=60)
    reserva=models.DateField()
    pago=models.BooleanField()

    def __str__(self):
        return f"Reserva {self.reserva}"