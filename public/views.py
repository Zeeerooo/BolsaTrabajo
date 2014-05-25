# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.decorators.http import require_GET, require_POST
from django.template import RequestContext
from public.forms import *
from django.http import HttpResponse
from django.contrib import messages

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
    signUpForm = SignUpForm()
    loginForm = LoginForm(request.POST)
    if not loginForm.is_valid():
        messages.add_message(request, messages.ERROR, 'E-mail o contraseña incorrectos')
        #return render_to_response('login.html', {"loginForm": loginForm, "signUpForm": signUpForm, "messages": messages}, context_instance = RequestContext(request))
    return render_to_response('login.html', {"loginForm": loginForm, "signUpForm": signUpForm}, context_instance = RequestContext(request))


'''
form = LoginForm(request.POST)
    if not form.is_valid():
        messages.add_message(request, messages.ERROR, _(u'E-mail o contraseña incorrectos'))
        t = get_template('login.html')
        context = RequestContext(request,{"form":form})
        return HttpResponse(t.render(context), status = 400)
        #return render_to_response('login.html', {"form": form}, context_instance = RequestContext(request), status=400)
    email = form.cleaned_data['email']
    password = form.cleaned_data['password']
    user = authenticate(username=email, password=password) # a pesar de que ahora se autentica con el mail, el campo que se ofrece a la funcion authenticate sigue siendo username
    if user is not None:
        if not user.is_active:
            messages.add_message(request, messages.ERROR, mark_safe(_(u'Usuario no activo. Deseas reenviar el correo de confirmación? Click <a href="/user/register/emailconfirmation/">aquí</a>')))
        else:
            #a partir de aqui el usuario se logueo exitosamente
            login(request, user)
            if request.POST.get('remember', None):
                request.session.set_expiry(0)
            try:
                request.session['django_language'] = user.user_data.language
            except AttributeError:
                pass
            except User_Data.DoesNotExist:
                pass
            #Se redirige a distintas paginas segun el rol del usuario
            return dashboardGroup(request, user)
    else:
        messages.add_message(request, messages.ERROR, _(u'E-mail o contraseña incorrectos'))
    t = get_template('login.html')
    context = RequestContext(request,{"form":form})
    return HttpResponse(t.render(context), status = 400)
    #return render_to_response('login.html', {"form": form}, context_instance = RequestContext(request))

'''




#Ofertas

@require_GET
def offerView(request):
    '''
        loginView genera la vista de login y loguea al usuario si no esta logueado
    '''
    loginForm = LoginForm()
    offerForm = AddOfferForm()
    return render_to_response('oferta.html', {"loginForm": loginForm, "offerForm": offerForm}, context_instance = RequestContext(request))


@require_POST
def offerView_post(request):
    '''
        Retorna al formulario de ingreso cuando ingresa una oferta mal, indica el error
    '''
    #return HttpResponse(t.render(context), status = 400)
    loginForm = LoginForm()
    offerForm = AddOfferForm(request.POST)
    if not offerForm.is_valid():
        #return HttpResponse("Error")
        return render_to_response("oferta.html", {"loginForm": loginForm, "offerForm": offerForm}, context_instance = RequestContext(request))
    else:
        return HttpResponse("No hay Error")
        #return render_to_response('index.html',  context_instance = RequestContext(request))
