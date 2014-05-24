# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.decorators.http import require_GET, require_POST
from django.template import RequestContext
from public.forms import *
from django.http import HttpResponse

@require_GET
def index(request):
    '''
        index invoca a la pagina index.html, la pagina de inicio
    '''
    loginForm = LoginForm()
    #return render_to_response('index.html', context_instance = RequestContext(request))
    return render_to_response('index.html', {"loginForm": loginForm}, context_instance = RequestContext(request))


@require_GET
def loginView(request):
    '''
        loginView genera la vista de login y loguea al usuario si no esta logueado
    '''
    loginForm = LoginForm()
    signUpForm = SignUpForm()
    return render_to_response('login.html', {"loginForm": loginForm, "signUpForm": signUpForm}, context_instance = RequestContext(request))


@require_POST
def loginView_post(request):
    '''
        Retorna al formulario de ingreso cuando se han logueado mal, indica el error
    '''
    #return HttpResponse(t.render(context), status = 400)
    loginForm = LoginForm()
    signUpForm = SignUpForm()
    errors = {"malo": "error"}
    return render_to_response('login.html', {"loginForm": loginForm, "signUpForm": signUpForm, "messages": errors}, context_instance = RequestContext(request))


#Ofertas

@require_GET
def offerView(request):
    '''
        loginView genera la vista de login y loguea al usuario si no esta logueado
    '''
    offerForm = AddOfferForm()
    return render_to_response('oferta.html', {"offerForm": offerForm}, context_instance = RequestContext(request))


@require_POST
def offerView_post(request):
    '''
        Retorna al formulario de ingreso cuando ingresa una oferta mal, indica el error
    '''
    #return HttpResponse(t.render(context), status = 400)

    form = AddOfferForm(request.POST)
    if not form.is_valid():
        #return HttpResponse("Error")
        return render_to_response("oferta.html", {"offerForm": form}, context_instance = RequestContext(request))
    else:
        return HttpResponse("No hay Error")
        #return render_to_response('index.html',  context_instance = RequestContext(request))
