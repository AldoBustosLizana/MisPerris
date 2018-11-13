
from django.contrib import admin
from django.conf.urls import url,include
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
=======
    path('registration/password_reset_form.html', PasswordResetView, name='resetForm'),
    path('accounts/',include('django.contrib.auth.urls'), name='index'),
>>>>>>> 2b258fb83e838474bf407f6c884c9a898e65f387
    path('registration/password_reset_form.html', PasswordResetView, name='resetForm'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('perro/', include ('Apps.perro.urls' )),
    path('reset/password_reset',auth_views.PasswordResetView.as_views, {'template_name':'registration/password_reset_form.html',
    'email_template_name':'registration/password_reset_email.html'}),
    path('reset/password_reset_done',PasswordResetDoneView,{'template_name': 'registration/password_reset_done.html'}),
    path('reset/(?P<uidba64>[0-9A-Za-z_\-]+)/(?P<token>.+)$', PasswordResetConfirmView,{'template_name':'registration/password_reset_confirm.html'}),
    path('reset/done',PasswordResetCompleteView,{'template_name': 'registration/password_reset_complete.html'}),
    path('', include ('Apps.perro.urls')),
<<<<<<< HEAD
    path('', include ('Apps.adopcion.urls')),
]  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('', include ('Apps.adopcion.urls'))
]
  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
>>>>>>> 2b258fb83e838474bf407f6c884c9a898e65f387
