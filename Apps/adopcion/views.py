from django.shortcuts import render, redirect, get_object_or_404

from Apps.adopcion.forms import RegistroPersona

from Apps.adopcion.models import Adopcion

def lista_Personas(request):
    if request.method == 'POST':
        form = RegistroPersona(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('registroPersonas')
    else:
        form = RegistroPersona()
    
    return render(request, 'MisPerris/registroPersona.html', {'form':form})

def registro_Personas(request):
    adopcion = Adopcion.objects.all()
    contexto = {'adopcion':adopcion}
    return render (request, 'MisPerris/listaPersona.html', contexto)

def editar_Personas(request, id_adopcion):
    adopcion = Adopcion.objects.get(id=id_adopcion)
    if request.method == 'GET':
        form = RegistroPersona(instance=adopcion)
    else:
        form = RegistroPersona(request.POST, instance=adopcion)
        if form.is_valid():
            form.save()
        return redirect('registroPersonas')
    return render(request, 'MisPerris/registroPersona.html', {'form':form})

def eliminar_Personas(request, id_adopcion):
    adopcion = Adopcion.objects.get(id=id_adopcion)
    if request.method == "POST":
        adopcion.delete()
        return redirect('registroPersonas')
    return render(request, 'MisPerris/eliminarPersona.html', {'adopcion':adopcion})
