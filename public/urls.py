from django.conf.urls import patterns, url, include

import views

METHOD_DISPATCHER = 'public.views_utils.method_dispatcher'

urlpatterns = patterns('',
    url(r'^catalogo/', include('normal_user.urls')),


    url(r'^login/', METHOD_DISPATCHER, {'GET': views.loginView, 'POST': views.loginView_post}, name='login'),
# Redirecciona a la vista del login
    url(r'','public.views.index', name='index'),
# Redirecciona a la vista de la pagina contacto ubicada en la carpeta templates, llamando a la funcion adkintun (Ah, si si) en el archivo view.py
)
