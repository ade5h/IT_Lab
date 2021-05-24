# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from webapp.forms import InputForm

# Create your views here.
def index(request):
	if request.method =='POST': 
		details = InputForm(request.POST)

		if details.is_valid():
			username = details.cleaned_data.get('username')
			email = details.cleaned_data.get('email')
			contact_number = details.cleaned_data.get('contact_number')

			return render(request, "success.html", {
				'username': username,
				'email': email,
				'contact_number': contact_number
			})

	else:
		context = {}
		context['form'] = InputForm()
		return render(request, "register.html", context)