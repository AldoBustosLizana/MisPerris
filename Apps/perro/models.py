from django.db import models
from django.utils import timezone

from Apps.adopcion.models import Persona

# Create your models here.

class Perro(models.Model):
	nombre = models.CharField(max_length = 50)
	raza = models.CharField(max_length = 30)
	descripcion = models.CharField(max_length = 100)
	estado = models.CharField(max_length = 20)
	fotografia = models.CharField(max_length = 20)
	persona = models.ForeignKey(Persona, null = True, on_delete = models.CASCADE)