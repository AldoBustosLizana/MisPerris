
from django.contrib import admin
from django.conf.urls import url,include
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^perro/', include ('Apps.perro.urls' )),
    url(r'^usuario/',include('Apps.usuarios.urls')),
    url(r'^$',LoginView,{'template_name':'login.html'}, name="login")
]

