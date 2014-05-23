# -*- coding: utf-8 -*-
from django import forms
from public.models import *
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
        Metodo que se encarga de definir los campos que tendra el formulario de login
    """
    email = forms.EmailField(label='Ingresa tu email', required=True, error_messages={'required': 'Campo Obligatorio'} , widget=forms.TextInput(attrs={'type':'email', 'placeholder': 'Email', 'class' : 'datostoken form-control input-lg' }))
    password = forms.CharField(label='Ingresa tu contraseña', required=True, error_messages={'required': 'Campo Obligatorio'}, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class' : 'datostoken form-control input-lg'}))
