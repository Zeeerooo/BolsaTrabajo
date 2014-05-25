# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
#DB
from public.models import Offer_Type

def catalogo(request, active_tab=None):
	#return HttpResponse("Here's the text of the Web page.")

	categories = Offer_Type.objects.all()
	#recuperar ofertas de bd
	jobs = [1,2,3,4,5,6]

	#diccionario para la vista
	data = {'jobs':jobs, 'active_tab':active_tab, 'categories':categories}
	return render_to_response('catalogo.html', data, context_instance = RequestContext(request))

def show_offer(request, offer_id):
	#return HttpResponse("Mostrar oferta completa." + offer_id)
	return render_to_response('oferta_full.html', None, context_instance = RequestContext(request))

def user_preferences(request):
	return HttpResponse("Sitio de user_preferences.")

def logout(request):
	return HttpResponse("Sistema de Logout.")
