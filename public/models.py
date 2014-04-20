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
	date = models.DateTimeField(default=datetime.now)
	description = models.CharField(max_length=2000)
	enterprise = models.CharField(max_length=50)
	part_time = models.BooleanField(default=False)
	full_time = models.BooleanField(default=False)
	practice = models.BooleanField(default=False)
	directed_work = models.BooleanField(default=False)

	def __unicode__(self):
		return self.enterprise + " " + self.date
