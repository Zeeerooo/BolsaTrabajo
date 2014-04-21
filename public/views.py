from django.shortcuts import render_to_response
from django.views.decorators.http import require_GET
from django.template import RequestContext

@require_GET
def index(request):
    '''
        index invoca a la pagina index.html, la pagina de inicio
    '''
    return render_to_response('index.html', context_instance = RequestContext(request))
