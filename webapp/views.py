from django.shortcuts import render, redirect
from .forms import InputForm

def index(request):
	form = InputForm()
	return render(request, 'firstPage.html', {'form': form})

def first_page(request):
	if request.method == 'POST':
		form = InputForm(request.POST)
		
		if form.is_valid():
			name = form.cleaned_data['name']
			roll = form.cleaned_data['roll']
			subject = form.cleaned_data['subject']

			request.session['name'] = name
			request.session['roll'] = roll
			request.session['subject'] = subject
		
	return redirect('/second_page')

def second_page(request):
	name = request.session['name']
	roll = request.session['roll']
	subject = request.session['subject']

	context = {'name': name, 'roll': roll, 'subject': subject}

	return render(request, 'secondPage.html', context)