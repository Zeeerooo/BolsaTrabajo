from django.conf.urls import patterns, url, include

from public.views import *

urlpatterns = patterns('',
    url(r'','public.views.index', name='index'),#redirecciona a la vista de la pagina contacto ubicada en la carpeta templates, llamando a la funcion adkintun en el archivo view.py
)