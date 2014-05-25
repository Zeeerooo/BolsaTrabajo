from django.conf.urls import patterns, url, include

import views

urlpatterns = patterns('',
	url(r'logout/','normal_user.views.logout', name='logout'),
	url(r'datos_usuario/','normal_user.views.user_preferences', name='user_preferences'),
	url(r'oferta/(?P<offer_id>[0-9]+)/$', 'normal_user.views.show_offer', name='show_offer'),
	url(r'^(?P<active_tab>(.*))/$', 'normal_user.views.catalogo', name='catalogo'),
	url(r'','normal_user.views.catalogo', name='catalogo'),
)
