from django import forms
from django.forms import widgets
from django.forms.fields import CharField, IntegerField

subjects = [
	('Math', 'Math'),
	('Physics', 'Physics'),
	('English', 'English'),
	('Chemistry', 'Chemistry'),
]
class InputForm(forms.Form):
	name = CharField()
	roll = IntegerField()
	subject = CharField(label='Select subject.',
	widget=forms.Select(choices=subjects))