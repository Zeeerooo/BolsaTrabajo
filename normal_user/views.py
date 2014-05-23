# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def catalogo(request):
    #return HttpResponse("Here's the text of the Web page.")
    jobs = [1,2,3,4,5]
    return render_to_response('catalogo.html', {'jobs':jobs}, context_instance = RequestContext(request))
