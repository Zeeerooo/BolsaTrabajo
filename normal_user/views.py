# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def catalogo(request):
	#return HttpResponse("Here's the text of the Web page.")
	
	#Recuperar datos de usuario
	user = "alguien@dcc.uchile.cl"

	#Recuperar datos de consulta a la bd
	active_tab = "Practicas II"
	categories = ["Trabajos Full-Time","Trabajos Part-Time","Practicas I","Practicas II","Trabajos FreeLance","Trabajos Dirijidos", "Todas las Ofertas"]

	#recuperar ofertas de bd
	jobs = [1,2,3,4,5,6,7]

	#diccionario para la vista
	data = {'user':user, 'jobs':jobs, 'active_tab':active_tab, 'categories':categories}

	return render_to_response('catalogo.html', data, context_instance = RequestContext(request))

def user_preferences(request):
	return HttpResponse("Sitio de user_preferences.")

def logout(request):
	return HttpResponse("Sistema de Logout.")
