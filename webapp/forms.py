from django import forms

CHOICES=[('HP','HP'),
         ('Nokia','Nokia'),
         ('Samsung','Samsung'),
         ('Motorola','Motorola'),
				 ('Apple', 'Apple')
				]

FAVORITE_COLORS_CHOICES = [
    ('Mobile', 'Mobile'),
    ('Laptop', 'Laptop')
]

class InputForm(forms.Form):
	company = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

	device = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )

	quantity = forms.CharField(max_length = 200);
