from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from .views import index,views, index_logged_out


urlpatterns = [
    #path('/login', LoginView.as_view(), name="login"),
    #path('', views.index, name='index2'),
    path('', LoginView.as_view(), name='index2'),
    path('contacto.html', views.contacto, name='contacto'),
    path('home', views.index, name='home'),
    path('registroPerros.html', views.lista_Perros, name='nuevoPerro'),
    path('listaPerros.html', views.registro_Perros, name='registroPerros'),
    path('editar/<int:id_perro>/', views.editar_Perros, name='editarPerros'),
    path('eliminar/<int:id_perro>/', views.eliminar_Perros, name='eliminarPerros'),
]