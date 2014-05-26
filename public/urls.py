from django.conf.urls import patterns, url, include

import views

METHOD_DISPATCHER = 'public.views_utils.method_dispatcher'

urlpatterns = patterns('',
    url(r'^catalogo/', include('normal_user.urls')),
    url(r'^signup/',   METHOD_DISPATCHER, {'GET': views.loginView, 'POST': views.signup}, name='signup'),
    url(r'^oferta/', METHOD_DISPATCHER, {'GET': views.offerView, 'POST': views.offerView_post}, name='oferta'),
    url(r'^login/', METHOD_DISPATCHER, {'GET': views.loginView, 'POST': views.loginView_post}, name='login'),
    url(r'^confirmarOferta/$', 'public.views.index', name='offer_confirmation' ),
    url(r'^confirmarOferta/([a-zA-Z0-9_]+)$', 'public.views.offer_confirmation', name='nuncausaremosesto' ),
    url(r'^validarUsuario/$', 'public.views.index', name='user_validation' ),
    url(r'^validarUsuario/([a-zA-Z0-9_]+)$', 'public.views.user_validation', name='nuncausaremosestotampoco' ),
   
# Redirecciona a la vista del login

    url(r'','public.views.index', name='index'),
# Redirecciona a la vista de la pagina contacto ubicada en la carpeta templates, llamando a la funcion adkintun (Ah, si si) en el archivo view.py
)
