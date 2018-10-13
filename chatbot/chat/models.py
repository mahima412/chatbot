# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# import Date
# Create your models here.
class DataResponse(models.Model):
	input_text = models.CharField(max_length=100)
	output_text = models.CharField(max_length=100)
	hidden = models.BooleanField(default=False)
	# created_at = models.DateField() 
	def __str__(self):
		return self.input_text
