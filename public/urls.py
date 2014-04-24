from django.conf.urls import patterns, url, include

import views

METHOD_DISPATCHER = 'public.views_utils.method_dispatcher'

urlpatterns = patterns('',
    url(r'^login/', METHOD_DISPATCHER, {'GET': views.loginView, 'POST': views.loginView_post}, name='login'),#redirecciona a la vista del login
    url(r'','public.views.index', name='index'),#redirecciona a la vista de la pagina contacto ubicada en la carpeta templates, llamando a la funcion adkintun en el archivo view.py
)