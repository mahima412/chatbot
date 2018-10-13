# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DataResponse
import random
# Create your views here.
# @csrf_exempt
def chat(request):	
	if request.method == "GET":		
		return render(request,'chat.html')

	if request.method == "POST":
		response_text_list = []
		response_text = ''
		message = ''

		query_text = str(request.POST.get('query_text')).strip()
		obj_data = DataResponse.objects.filter(input_text=query_text.lower())
		if obj_data:
			status = 1
			for data in obj_data:
				response_text_list.append(data.output_text)	
		else:
			status = 0
			message = "Opps!! I did't get you, Please ask some other things."

		if status == 1:
			response_text = random.choice(response_text_list)
		response={'status':status,
				  'message':message,
				  'response_text':response_text}
		return JsonResponse(response)
