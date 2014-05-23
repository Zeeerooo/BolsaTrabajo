from django.conf.urls import patterns, url, include

import views

urlpatterns = patterns('',
		url(r'logout/','normal_user.views.logout', name='logout'),
		url(r'datos_usuario/','normal_user.views.user_preferences', name='user_preferences'),
    url(r'','normal_user.views.catalogo', name='catalogo'),
)
