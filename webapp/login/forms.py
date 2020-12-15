from django import forms
from django.forms import ModelForm

from .models import *

class  DateInput(forms.DateInput):
	input_type = 'datetime'

class  TimeInput(forms.TimeInput):
	input_type = 'time'

class ulogin(forms.Form):
	Unm = forms.EmailField(max_length=100)
	pwd = forms.CharField(widget=forms.PasswordInput,max_length=32)

class reg(forms.ModelForm):
	password = forms.CharField(max_length=10,widget=forms.PasswordInput)
	class Meta:
	 	model = UserData
	 	fields = '__all__'

class TaskForm(forms.ModelForm):
	
	class Meta:
	 	model = Taskdet
	 	fields=['title','complete']

	