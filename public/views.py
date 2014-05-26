# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.decorators.http import require_GET, require_POST
from django.template import RequestContext
from public.forms import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from string import letters
from datetime import timedelta
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
#BD
from public.models import Offer
from normal_user.models import EmailConfirmation


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
    if request.user.is_authenticated():
        return render_to_response('index.html', {"loginForm": loginForm}, context_instance = RequestContext(request))
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
        messages.add_message(request, messages.ERROR, 'Formulario Incompleto')
        return render_to_response('login.html', {"loginForm": loginForm, "signUpForm": signUpForm}, context_instance = RequestContext(request))
    email = loginForm.cleaned_data['email']
    password = loginForm.cleaned_data['password']
    user = authenticate(username=email, password=password) # a pesar de que ahora se autentica con el mail, el campo que se ofrece a la funcion authenticate sigue siendo username
    if user is not None:
        if not user.is_active:
            messages.add_message(request, messages.ERROR, 'Usuario no activo. Revisaste el correo de confirmación?')
        else:
            #a partir de aqui el usuario se logueo exitosamente
            login(request, user)
            #if request.POST.get('remember', None):
            #    request.session.set_expiry(0)
            #messages.add_message(request, messages.SUCCESS, 'Ingresado correctamente')
    else:
        messages.add_message(request, messages.ERROR, 'Email o contraseña incorrectos')
    return render_to_response('index.html', {"loginForm": loginForm, "signUpForm": signUpForm}, context_instance = RequestContext(request))

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
        #offerForm.save()
        data = offerForm.cleaned_data
        print data
        oferta = Offer(long_description=data['long_description'], short_description=data['short_description'], tecnologies=data['tecnologies'], institution=data['institution'], responsable=data['responsable'], mail=data['mail'], phone=data['phone'], length=data['length'], work_direction=data['work_direction'], salary=data['salary'])
        oferta.expire_date=oferta.date+ settings.OFFER_AVALAIBLE_DAYS
        oferta.verified=False
        oferta.save() #hay que grabarla antes de agregarla a confirmation y agregarle manytomany objects
        code = ''.join([choice(letters) for i in xrange(30)])
        confirmation = Offer_Confirmation(offer=oferta, code=code)
        confirmation.save()
        if 'offer_type' in data:
            for x in data['offer_type']:
                try:
                    o = Offer_Type.objects.get(id=x)
                    oferta.offer_type.add(o)
                except Offer_Type.DoesNotExist:
                    pass                
        oferta.save()

        #mandar mail
        email = oferta.mail
        url="http://"+request.get_host()+reverse('offer_confirmation')+ code
        html_content = render_to_string('confirmation/offer.html', {'url':url})
        text_content = strip_tags(html_content)
        subject = "Confirmación Oferta"
        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        
        return render_to_response('oferta_ingresada.html', {"loginForm" : loginForm,} ,context_instance = RequestContext(request))
        

@require_POST
def signup(request):
    '''
    ingresa los datos del usuario que se esta registrando
    '''
    print "comienzo la funcion"
    data = request.POST.copy() # so we can manipulate data
    # random username
    data['username'] = ''.join([choice(letters) for i in xrange(30)])
    form = SignUpForm(data)
    if not form.is_valid():
        messages.add_message(request, messages.ERROR, 'Complete correctamente los datos')
        loginForm = LoginForm()
        return render_to_response("login.html", {"loginForm":loginForm, "signUpForm": form}, context_instance = RequestContext(request))
    form.save()
    email = form.cleaned_data['email']
    password = form.cleaned_data['password1']
    user = User.objects.get(email=email)
    
    #envio mail
    code = ''.join([choice(letters) for i in xrange(40)])
    var = EmailConfirmation.objects.filter(user=user)
    if var:
        var.update(code=code)
    else:
        emailConfirmation = EmailConfirmation(user=user, code=code)
        emailConfirmation.save()    
    url="http://"+request.get_host()+reverse('user_validation')+code
    html_content = render_to_string('confirmation/user.html', {'url':url})
    text_content = strip_tags(html_content)
    subject = "Valida tu registro en Bolsa de TrabajoDCC"
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    user.is_active=False
    user.save()

    loginForm = LoginForm()
    return render_to_response('usuario_registrado.html', {"loginForm" : loginForm,} ,context_instance = RequestContext(request))


@require_GET
def offer_confirmation(request, code):
    loginForm = LoginForm()
    if code:
        try:
            confirmation = Offer_Confirmation.objects.get(code=code)
            offer = confirmation.offer
            offer.verified=True
            confirmation.delete()
            offer.save()
            return render_to_response('oferta_verificada.html',{"loginForm":loginForm},  context_instance = RequestContext(request))
        except Offer_Confirmation.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'Código de Oferta no existe')
    form = SignUpForm()
    return render_to_response("login.html", {"loginForm":loginForm, "signUpForm": form}, context_instance = RequestContext(request))


@require_GET
def user_validation(request, code):
    loginForm = LoginForm()
    if code:
        try:
            confirmation = EmailConfirmation.objects.get(code=code)
            user = confirmation.user
            user.is_active=True
            confirmation.delete()
            user.save()
            return render_to_response('usuario_validado.html',{"loginForm":loginForm},  context_instance = RequestContext(request))
        except EmailConfirmation.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'Código de Usuario no existe')
    form = SignUpForm()
    return render_to_response("login.html", {"loginForm":loginForm, "signUpForm": form}, context_instance = RequestContext(request))

