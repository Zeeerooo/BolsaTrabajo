# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
#DB
from public.models import Offer_Type, Offer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.urlresolvers import reverse

def catalogo(request, active_tab="Trabajo Full-Time"):

	try:
		selectedCategory = Offer_Type.objects.get(name=active_tab)
	except Offer_Type.DoesNotExist:
		selectedCategory = Offer_Type(name="Ver Todos", id=0)

	#Recuperar Categorias para barra de navegacion
	categories = Offer_Type.objects.all()
	#Recuperar ofertas según categoria seleccionada
	if(selectedCategory.id==0):
		jobs = Offer.objects.all()
	else:
		jobs = Offer.objects.filter(offer_type__id=selectedCategory.id)
	jobs = jobs.filter(verified=True)

	#diccionario para la vista
	data = {'jobs':jobs, 'selected_category':selectedCategory, 'categories':categories}
	return render_to_response('catalogo.html', data, context_instance = RequestContext(request))

def show_offer(request, offer_id):
	#return HttpResponse("Mostrar oferta completa." + offer_id)
	return render_to_response('oferta_full.html', None, context_instance = RequestContext(request))

def user_preferences(request):
	return HttpResponse("Sitio de user_preferences.")


@login_required(login_url='/login',redirect_field_name=None)
def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse("index"))
