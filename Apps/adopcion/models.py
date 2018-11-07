from django.db import models


# Create your models here.
class Persona(models.Model):
    rut = models.CharField(max_length = 8, primary_key = True)
    dv = models.CharField(max_length = 1)
    nombre = models.CharField(max_length = 50)
    apellidos = models.CharField(max_length = 80)
    fechaNacimiento = models.DateField()
    telefono = models.IntegerField()
    domicilio = models.CharField(max_length = 50)
    mail = models.CharField(max_length = 100)

