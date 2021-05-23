from django import forms

MANUFACTURERS = [
    ('bmw', 'BMW'),
    ('volkswagen', 'Volkswagen'),
    ('fordmotor', 'Ford Motor'),
    ('honda', 'Honda'),
  ]

class InputForm(forms.Form):
	manufacturer = forms.ChoiceField(choices = MANUFACTURERS)

	model_name = forms.CharField(max_length = 300) 