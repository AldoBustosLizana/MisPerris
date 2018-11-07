
from django.contrib import admin
from django.conf.urls import url,include
from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns = [
    url('^admin/', admin.site.urls),
    path('',include('Apps.usuarios.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    url(r'^perro/', include ('Apps.perro.urls' )),
    url(r'^usuario/',include('Apps.usuarios.urls')),
]

