# -*- coding: utf-8 -*-
from django import forms
from public.models import *
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
        Metodo que se encarga de definir los campos que tendra el formulario de login
    """
    email = forms.EmailField(label='Ingresa tu email', required=True, error_messages={'required': 'Campo Obligatorio'} , widget=forms.TextInput(attrs={'type':'email', 'placeholder': 'Correo @DCC', 'class' : 'form-control'}))
    password = forms.CharField(label='Ingresa tu contraseña', required=True, error_messages={'required': 'Campo Obligatorio'}, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class' : 'form-control'}))


class SignUpForm(forms.Form):
    """
        Metodo que se encarga de definir los campos que tendra el formulario de registro
    """
    email = forms.EmailField(label='Correo @DCC', required=True, error_messages={'required': 'Campo Obligatorio'} , widget=forms.TextInput(attrs={'type':'email', 'placeholder': 'Correo @DCC', 'class' : 'form-control'}))
    repeatEmail = forms.EmailField(label='Repetir Correo @DCC', required=True, error_messages={'required': 'Los correos deben coincidir'} , widget=forms.TextInput(attrs={'type':'email', 'placeholder': 'Repetir Correo @DCC', 'class' : 'form-control'}))
    password = forms.CharField(label='Ingresa tu contraseña', required=True, error_messages={'required': 'Campo Obligatorio'}, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class' : 'form-control'}))
    repeatPassword = forms.CharField(label='Repetir Contraseña', required=True, error_messages={'required': 'Contraseñas deben coincidir'}, widget=forms.PasswordInput(attrs={'placeholder': 'Repetir Contraseña', 'class' : 'form-control'}))
