from django import forms

from Apps.adopcion.models import Adopcion

class RegistroPersona(forms.ModelForm):
    class Meta:
        model = Adopcion
        
        fields = [
            'rut',
            'nombre',
            'apellidos',
            'fechaNacimiento',
            'telefono',
            'correo',
        ]

        labels = {
            'rut' : 'Rut',
            'nombre' : 'Nombre',
            'apellidos' : 'Apellidos',
            'fechaNacimiento' : 'FechaNacimiento',
            'telefono' : 'Telefono',
            'correo' : 'Correo',
        }
        
        widgets = {
            'rut' : forms.TextInput(attrs={'class':'form-control'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'apellidos' : forms.TextInput(attrs={'class':'form-control'}),
            'fechaNacimiento' : forms.TextInput(attrs={'class':'form-control'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control'}),
        }