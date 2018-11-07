
from django.contrib import admin
from django.conf.urls import url,include
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.urls import path

urlpatterns = [
    url('^admin/', admin.site.urls),
    path('',include('Apps.usuarios.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    url(r'^perro/', include ('Apps.perro.urls' )),
    url(r'^usuario/',include('Apps.usuarios.urls')),
    url(r'^reset/password_reset',PasswordResetView, {'template_name':'registration/password_reset_form.html',
    'email_template':'registration/password_reset_email.html'}),
    url(r'^reset/password_reset_done',PasswordResetDoneView,{'template_name': 'registration/password_reset_done.html'}),
    url(r'^reset/(?P<uidba64>[0-9A-Za-z_\-]+)/(?P<token>.+)$', PasswordResetConfirmView,{'template_name':'registration/password_reset_confirm.html'}),
    url(r'^reset/done',PasswordResetCompleteView,{'template_name': 'registration/password_reset_complete.html'})
]

