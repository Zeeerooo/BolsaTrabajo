from django.http import Http404


def method_dispatcher(request, *args, **kwargs):
    '''
        Metodo que redirige al metodo correspondiente segun el metodo de request
    '''
    get_view = kwargs.pop('GET', None)
    post_view = kwargs.pop('POST', None)
    if request.method == 'GET' and get_view is not None:
        return get_view(request, *args, **kwargs)
    elif request.method == 'POST' and post_view is not None:
        return post_view(request, *args, **kwargs)
    raise Http404