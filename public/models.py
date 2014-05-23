# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from random import choice
from string import printable
from datetime import datetime


class Offer(models.Model):
	'''
	Esta clase define las ofertas desplegadas en la pagina.
	id: identificador unico 
	date: fecha de la creacion 
	description: Descripcion completa de la oferta 
	enterprise: Empresa desde la cual proviene la oferta 
	part_time: booleano para categorizar a la oferta como de tipo part-time
	full_time: booleano para categorizar a la oferta como de tipo full-time 
	practice:  booleano para categorizar a la oferta como de tipo practica
	directed_work: booleano para categorizar a la oferta como de tipo trabajo dirigido
	'''
	id = models.CharField(primary_key=True, default = ''.join([choice(printable) for i in xrange(20)]), max_length=20 )

	long_description = models.CharField(max_length=2000, blank=True)
	short_description = models.CharField(max_length=140, blank=True)
	tecnologies = models.CharField(max_length=500, blank=True)
	date = models.DateTimeField(default=datetime.now)
	expire_date = models.DateTimeField(default=datetime.now)
	institution = models.CharField(max_length=100, blank=True)
	responsable = models.CharField(max_length=100)
	mail = models.EmailField(max_length=70, blank=True)
	phone = models.CharField(max_length=20, blank=True)
	length = models.CharField(max_length=30, blank=True)
	work_direction = models.CharField(max_length=30, blank=True)
	offer_type = models.ManyToManyField("Offer_Type", blank=True, null=True)
	verified = models.BooleanField(default=True)

	def __unicode__(self):
		return self.institution + " - " + self.date

class Offer_Type(models.Model):
	'''
	Tipos de ofertas permitidos
	'''
	id = models.IntegerField(primary_key=True, max_length=1)
	name = models.CharField(max_length=100)

