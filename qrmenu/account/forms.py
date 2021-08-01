from django import forms
from restaurant.models import Meal

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class MealAddForm(forms.ModelForm):
	class Meta:
		model = Meal
		exclude = ['restaurant',]
