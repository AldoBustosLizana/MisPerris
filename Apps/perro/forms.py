from django import forms

from Apps.perro.models import Perro

class RegistroPerro(forms.ModelForm):
    class Meta:
        model = Perro
        
        fields = [
            'nombre',
            'raza',
            'descripcion',
            'estado',
            'fotografia',
        ]

        labels = {
            'nombre' : 'Nombre',
            'raza' : 'Raza',
            'descripcion' : 'Descripcion',
            'estado' : 'Estado',
            'fotografia' : 'Fotografia',
        }
        
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'raza' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
            'estado' : forms.TextInput(attrs={'class':'form-control'}),
        }