
from django.contrib import admin
from django.conf.urls import url,include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^perro/', include ('Apps.perro.urls')),
    url(r'^usuario/',include('Apps.usuarios.urls')),
]

