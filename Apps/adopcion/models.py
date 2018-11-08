from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils import timezone

# Create your models here.
class Adopcion(models.Model):
    rut = models.CharField(max_length = 8)
    nombre = models.CharField(max_length = 50)
    apellidos = models.CharField(max_length = 80)
    fechaNacimiento = models.DateField()
    telefono = models.CharField(max_length = 9)
    correo = models.CharField(max_length = 9)
    