from django.urls import path

from . import views

urlpatterns = [
    path('registroPersona.html', views.lista_Personas, name='nuevaPersona'),
    path('listaPersona.html', views.registro_Personas, name='registroPersonas'),
    path('editarPersona/<int:id_adopcion>/', views.editar_Personas, name='editarPersonas'),
    path('eliminarPersona/<int:id_adopcion>/', views.eliminar_Personas, name='eliminarPersonas'),
]