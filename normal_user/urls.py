from django.conf.urls import patterns, url, include

import views

urlpatterns = patterns('',
    url(r'','normal_user.views.catalogo', name='catalogo'),
)
