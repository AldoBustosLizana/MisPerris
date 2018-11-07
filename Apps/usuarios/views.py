from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = UserCreationForm
    