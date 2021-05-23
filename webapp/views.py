# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import InputForm

# Create your views here.
def index(request):
	if request.method =='POST': 
		details = InputForm(request.POST)

		if details.is_valid():
			manufacturer = details.cleaned_data.get('manufacturer')
			model_name = details.cleaned_data.get('model_name')
			return render(request, "render.html", {
				'manufacturer': manufacturer,
				'model_name': model_name
			})

	else:
		context = {}
		context['form'] = InputForm()
		return render(request, "basic.html", context)