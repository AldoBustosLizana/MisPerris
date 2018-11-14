from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

# Create your models here.
class Adopcion(models.Model):
    rut = models.CharField(max_length = 8)
    dv = models.CharField(max_length = 1)
    nombre = models.CharField(max_length = 30)
    apellidos = models.CharField(max_length = 50)
    fechaNacimiento = models.DateField()
    telefono = models.CharField(max_length = 9)
    correo = models.CharField(max_length = 50)