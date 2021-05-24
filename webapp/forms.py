from django import forms

class InputForm(forms.Form):
	username = forms.CharField(max_length = 100)
	password = forms.CharField(widget = forms.PasswordInput(), required = False)
	email = forms.EmailField(max_length = 200, required = False)
	contact_number = forms.IntegerField(required = False)