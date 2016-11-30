# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from phonenumber_field.modelfields import PhoneNumberField

class MyPortfolio(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	image = models.ImageField(upload_to = 'images/')
	website = models.URLField(max_length=500)
	date = models.DateTimeField()

	def __str__(self):
		return self.title
	

# class bio(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=40)
#     mobile = models.PhoneNumberField(max_length=13)
#     email = models.EmailField()
#     education = models.TextField()
