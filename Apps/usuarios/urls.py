from django.conf.urls import url
from Apps.usuarios.views import RegistroUsuario
from . import views
from django.urls import path

urlpatterns = [
    url(r'^registrar',RegistroUsuario.as_view()),
    path('',views.index, name='index'),
]
