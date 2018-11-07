from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto.html', views.contacto, name='contacto'),
]