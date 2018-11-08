from django.urls import path

from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('',views.index_login),
    path('contacto.html', views.contacto, name='contacto'),
]