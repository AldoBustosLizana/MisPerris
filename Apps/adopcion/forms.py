from django import forms

from Apps.adopcion.models import Adopcion

class RegistroPersona(forms.ModelForm):
    class Meta:
        model = Adopcion
        
        fields = [
            'rut',
            'dv',
            'nombre',
            'apellidos',
            'fechaNacimiento',
            'telefono',
            'correo',
        ]

        labels = {
            'rut' : 'Rut',
            'dv' : 'Dv',
            'nombre' : 'Nombre',
            'apellidos' : 'Apellidos',
            'fechaNacimiento' : 'FechaNacimiento',
            'telefono' : 'Telefono',
            'correo' : 'Correo',
        }
        
        widgets = {
            'rut' : forms.TextInput(attrs={'placeholder':'Ej. 18516163', 'onkeypress':'return validarNumeros(event)', 'class':'form-control'}),
            'dv' : forms.TextInput(attrs={'onblur':'validarRut(rut, dv)', 'onkeypress':'return validarDigito(event)', 'class':'form-control'}),
            'nombre' : forms.TextInput(attrs={'onkeypress':'return validarLetrasConEspacio(event)', 'class':'form-control'}),
            'apellidos' : forms.TextInput(attrs={'onkeypress':'return validarLetrasConEspacio(event)', 'class':'form-control'}),
            'fechaNacimiento' : forms.TextInput(attrs={'max':'2001-12-31','value':'2001-12-31','autocomplete':'on', 'onblur':'validarAnno(fechaNacimiento)','class':'form-control'}),
            'telefono' : forms.TextInput(attrs={'onkeypress':'return validarNumeros(event)', 'class':'form-control'}),
            'correo' : forms.TextInput(attrs={'class':'form-control'}),
        }