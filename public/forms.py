# -*- coding: utf-8 -*-
from django import forms
from public.models import *
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
        Clase que se encarga de definir los campos que tendra el formulario de login
    """
    email = forms.EmailField(label='Ingresa tu email', required=True, error_messages={'required': 'Campo Obligatorio'} , widget=forms.TextInput(attrs={'type':'email', 'placeholder': 'Correo @DCC', 'class' : 'form-control'}))
    password = forms.CharField(label='Ingresa tu contraseña', required=True, error_messages={'required': 'Campo Obligatorio'}, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class' : 'form-control'}))


class SignUpForm(forms.Form):
    """
        Clase que se encarga de definir los campos que tendra el formulario de registro
    """
    email = forms.EmailField(label='Correo @DCC', required=True, error_messages={'required': 'Campo Obligatorio'} , widget=forms.TextInput(attrs={'type':'email', 'placeholder': 'Correo @DCC', 'class' : 'form-control'}))
    repeatEmail = forms.EmailField(label='Repetir Correo @DCC', required=True, error_messages={'required': 'Los correos deben coincidir'} , widget=forms.TextInput(attrs={'type':'email', 'placeholder': 'Repetir Correo @DCC', 'class' : 'form-control'}))
    password = forms.CharField(label='Ingresa tu contraseña', required=True, error_messages={'required': 'Campo Obligatorio'}, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class' : 'form-control'}))
    repeatPassword = forms.CharField(label='Repetir Contraseña', required=True, error_messages={'required': 'Contraseñas deben coincidir'}, widget=forms.PasswordInput(attrs={'placeholder': 'Repetir Contraseña', 'class' : 'form-control'}))


DATA_CHOICES={(0,1)}

class AddOfferForm(forms.Form):
    """
        Clase que se encargará de definir los campos para el formulario de agregar ofertas
    """

    long_description = forms.CharField(label="Descripción Larga",max_length=2000, error_messages={'required': 'Campo Obligatorio'}, widget=forms.TextInput(attrs={'type':'text', 'placeholder': 'Ingrese aquí su descripción', 'class' : 'form-control'}))
    short_description = forms.CharField(label="Descripción Corta",max_length=140, error_messages={'required': 'Campo Obligatorio'}, widget=forms.TextInput(attrs={'type':'text', 'placeholder': 'Ingrese aquí su descripción de máximo 140 caracteres', 'class' : 'form-control'}))
    tecnologies = forms.CharField(label="Tecnologías requeridas",max_length=500, required=False, widget=forms.TextInput(attrs={'type':'text', 'placeholder': 'Ej: Java', 'class' : 'form-control'}))
    institution = forms.CharField(label="Nombre de Institución",max_length=100, error_messages={'required': 'Campo Obligatorio'}, widget=forms.TextInput(attrs={'type':'text', 'class' : 'form-control'}))
    responsable = forms.CharField(label="Nombre persona responsable",max_length=100, error_messages={'required': 'Campo Obligatorio'}, widget=forms.TextInput(attrs={'type':'text', 'class' : 'form-control'}))
    mail = forms.EmailField(label='Correo de Contacto', max_length=70, error_messages={'required': 'Campo Obligatorio'} , widget=forms.TextInput(attrs={'type':'email', 'placeholder': 'Ej: ejemplo@dcc.cl', 'class' : 'form-control'}))
    phone = forms.RegexField(label='Teléfono de Contacto',max_length=20, required=False, regex=r'^[0-9]+$', error_messages={"invalid": "Sólo debe ingresar números"}, widget=forms.TextInput(attrs={'type':'text', 'placeholder': 'Telefono', 'class' : 'form-control'}))
    length = forms.CharField(label='Duración del Trabajo',max_length=30, required=False, widget=forms.TextInput(attrs={'type':'text', 'placeholder': 'Ej: 1 año', 'class' : 'form-control'}))
    work_direction = forms.CharField(label='Dirección de Trabajo',max_length=30, required=False, widget=forms.TextInput(attrs={'type':'text', 'placeholder': 'Dirección', 'class' : 'form-control'}))
    #offer_type = forms.ManyToManyField()

    offer_type = forms.ChoiceField(choices=DATA_CHOICES, widget=forms.RadioSelect(attrs={'required':'true'}), required=True, error_messages={'required': 'Elija una de las opciones'})
