# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.decorators.http import require_GET, require_POST
from django.template import RequestContext
from public.forms import *

@require_GET
def index(request):
    '''
        index invoca a la pagina index.html, la pagina de inicio
    '''
    return render_to_response('index.html', context_instance = RequestContext(request))


@require_GET
def loginView(request):
    '''
        loginView genera la vista de login y loguea al usuario si no esta logueado
    '''
    form = LoginForm()
    return render_to_response('login.html', {"form": form}, context_instance = RequestContext(request))


@require_POST
def loginView_post(request):
    '''
        Retorna al formulario de ingreso cuando se han logueado mal, indica el error
    '''
    return HttpResponse(t.render(context), status = 400)
    