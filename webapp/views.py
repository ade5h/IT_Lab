# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from webapp.forms import InputForm

# Create your views here.
def index(request):
	if request.method =='POST': 
		details = InputForm(request.POST)

		if details.is_valid():
			company = details.cleaned_data.get('company')
			device = details.cleaned_data.get('device')[0]
			quantity = details.cleaned_data.get('quantity')

			print(company)
			print(device)
			print(quantity)

			priceDetails = {
				'Nokia': {'Laptop': 20, 'Mobile': 5},
				'HP': {'Laptop': 25, 'Mobile': 6},
				'Motorola': {'Laptop': 30, 'Mobile': 4},
				'Apple': {'Laptop': 60, 'Mobile': 20},
				'Samsung': {'Laptop': 50, 'Mobile': 10},
			}

			price = priceDetails[company][device]*int(quantity)

			return render(request, "purchaseDetails.html", {
				'company': company,
				'device': device,
				'quantity': quantity,
				'price': price
			})

	else:
		context = {}
		context['form'] = InputForm()
		return render(request, "buy.html", context)