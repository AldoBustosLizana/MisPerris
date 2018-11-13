from django.shortcuts import render, redirect, get_object_or_404

from Apps.perro.forms import RegistroPerro,forms
from .forms import forms
from Apps.perro.models import Perro

# Create your views here.
def index(request):
    return render(request, 'MisPerris/index.html')

def contacto(request):
    
    return render(request, 'MisPerris/contacto.html')

def index_login(request):
    return render(request,'registration/login.html')

def index_logged_out(request):
    return render(request, 'registration/logged_out.html')
    

def lista_Perros(request):
    if request.method == 'POST':
        form = RegistroPerro(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('registroPerros')
    else:
        form = RegistroPerro()
    
    return render(request, 'MisPerris/registroPerros.html', {'form':form})

def registro_Perros(request):
    perro = Perro.objects.all()
    contexto = {'perro':perro}
    return render (request, 'MisPerris/listaPerros.html', contexto)

def editar_Perros(request, id_perro):
    perro = Perro.objects.get(id=id_perro)
    if request.method == 'GET':
        form = RegistroPerro(instance=perro)
    else:
        form = RegistroPerro(request.POST, instance=perro)
        if form.is_valid():
            form.save()
        return redirect('registroPerros')
    return render(request, 'MisPerris/registroPerros.html', {'form':form})


def eliminar_Perros(request, id_perro):
    perro = Perro.objects.get(id=id_perro)
    if request.method == "POST":
        perro.delete()
        return redirect('registroPerros')
    return render(request, 'MisPerris/eliminarPerros.html', {'perro':perro})
