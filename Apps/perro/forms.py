from django import forms
from .models import Perro

class PostContacto(forms.ModelForm):
    class Meta:
        model = Perro
        fields = ('nombre', 'raza',)