from django.conf.urls import url
from Apps.usuarios.views import RegistroUsuario


urlpatterns = [
    url(r'^registrar',RegistroUsuario.as_view())
]