from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('',views.index_login),
    path('contacto.html', views.contacto, name='contacto'),
    path('registroPerros.html', views.lista_Perros, name='nuevoPerro'),
    path('listaPerros.html', views.registro_Perros, name='registroPerros'),
    path('editar/<int:id_perro>/', views.editar_Perros, name='editarPerros'),
    path('eliminar/<int:id_perro>/', views.eliminar_Perros, name='eliminarPerros'),
]