# -*- coding: utf-8 -*-
from django import forms
from public.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    """
        Clase que se encarga de definir los campos que tendra el formulario de login
    """
    email = forms.EmailField(label='Ingresa tu email', required=True, error_messages={'required': 'Campo Obligatorio'} , widget=forms.TextInput(attrs={'type':'email', 'placeholder': 'Correo @DCC', 'class' : 'form-control'}))
    password = forms.CharField(label='Ingresa tu contraseña', required=True, error_messages={'required': 'Campo Obligatorio'}, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class' : 'form-control'}))


class SignUpForm(UserCreationForm):
    """
        Clase que se encarga de definir los campos que tendra el formulario de registro
    """
    email = forms.EmailField(label='Correo @DCC', required=True, error_messages={'required': 'Campo Obligatorio'} , widget=forms.TextInput(attrs={'type':'email', 'placeholder': 'Correo @DCC', 'class' : 'form-control'}))
    #repeatEmail = forms.EmailField(label='Repetir Correo @DCC', required=True, error_messages={'required': 'Los correos deben coincidir'} , widget=forms.TextInput(attrs={'type':'email', 'placeholder': 'Repetir Correo @DCC', 'class' : 'form-control'}))
    password1 = forms.CharField(label='Ingresa tu contraseña', required=True, error_messages={'required': 'Campo Obligatorio'}, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class' : 'form-control'}))
    password2 = forms.CharField(label='Repetir Contraseña', required=True, error_messages={'required': 'Contraseñas deben coincidir'}, widget=forms.PasswordInput(attrs={'placeholder': 'Repetir Contraseña', 'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'username',)

    def clean_email(self):
        email = self.cleaned_data["email"]
        #email2 = self.cleaned_data["repeatEmail"]
        #if not email==email2:    
        #    raise forms.ValidationError('Emails no coinciden')
        try:
            User.objects.get(email=email)
            raise forms.ValidationError('Este e-mail ya está registrado.')
        except User.DoesNotExist:
            return email


#    def clean_password(self):
#        
#        password = self.cleaned_data["password"]
#        password2 = self.cleaned_data["password2"]
#        if not password==password2:    
#            raise forms.ValidationError('Passwords no coinciden')
#        return password


    def save(self, commit=True):
        print "paso por acuya" 
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.is_active = True # change to false if using email activation
        user.save()
        return user



DATA_CHOICES=(("1","Trabajo Full-Time"),  ("2",  "Trabajo Part-Time"),  ("3",  "Trabajo FreeLance"),  ("4",  "Trabajo Dirigido"),  ("5",  "Práctica I"),  ("6",  "Práctica II"))

class AddOfferForm(forms.Form):
    """
        Clase que se encargará de definir los campos para el formulario de agregar ofertas
    """
    short_description = forms.CharField(label="Descripción Corta",max_length=140, error_messages={'required': 'Campo Obligatorio'}, widget=forms.Textarea(attrs={'placeholder': 'Utilice este espacio para brindar una breve descripción de maximo 140 caracteres que ilustre la temática y objetivos del trabajo', 'class' : 'form-control', 'rows' : '3', 'onkeyup' : 'updateChars()'}))
    long_description = forms.CharField(label="Descripción Larga",max_length=2000, error_messages={'required': 'Campo Obligatorio'}, widget=forms.Textarea(attrs={'placeholder': 'Ingrese aquí todos los detalles de la oferta', 'class' : 'form-control', 'rows' : '5'}))
    tecnologies = forms.CharField(label="Tecnologías requeridas",max_length=500, required=False, widget=forms.TextInput(attrs={'type':'text', 'placeholder': 'Técnologías separadas por comas. Ej: PHP, Java, MySQL, SOA', 'class' : 'form-control'}))
    institution = forms.CharField(label="Empresa o Institución",max_length=100, error_messages={'required': 'Campo Obligatorio'}, widget=forms.TextInput(attrs={'type':'text', 'class' : 'form-control'}))
    responsable = forms.CharField(label="Nombre persona responsable",max_length=100, error_messages={'required': 'Campo Obligatorio'}, widget=forms.TextInput(attrs={'type':'text', 'class' : 'form-control'}))
    mail = forms.EmailField(label='Correo de Contacto', max_length=70, error_messages={'required': 'Campo Obligatorio'} , widget=forms.TextInput(attrs={'type':'email', 'placeholder': 'Ej: ejemplo@empresa.cl', 'class' : 'form-control'}))
    phone = forms.RegexField(label='Teléfono de Contacto',max_length=20, required=False, regex=r'^[0-9]+$', error_messages={"invalid": "Sólo debe ingresar números"}, widget=forms.TextInput(attrs={'type':'text', 'placeholder': '', 'class' : 'form-control'}))
    length = forms.CharField(label='Duración del Trabajo',max_length=30, required=False, widget=forms.TextInput(attrs={'type':'text', 'placeholder': 'Ej: 1 año', 'class' : 'form-control'}))
    work_direction = forms.CharField(label='Dirección de Trabajo',max_length=30, required=False, widget=forms.TextInput(attrs={'type':'text', 'placeholder': '', 'class' : 'form-control'}))
    salary = forms.CharField(label='Remuneración',max_length=30, required=False, widget=forms.TextInput(attrs={'type':'text', 'placeholder': 'Ej: 250.000 bruto', 'class' : 'form-control'}))
    #offer_type = forms.ManyToManyField()

    offer_type = forms.MultipleChoiceField(choices=DATA_CHOICES, widget=forms.CheckboxSelectMultiple())
