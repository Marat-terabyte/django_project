from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm



class registr_form(UserCreationForm):

	username = forms.CharField(max_length = 100 , widget = forms.TextInput(attrs={
		'class':'input_field',
		'placeholder':'Имя пользователя (уникальный)',
		'autocomplete':'off'
		}))


	first_name = forms.CharField(max_length = 50 , widget = forms.TextInput(attrs={
		'class':'input_field',
		'placeholder':'Имя',
		'autocomplete':'off'
		}))


	last_name = forms.CharField(max_length = 100 , widget = forms.TextInput(attrs={
		'class':'input_field',
		'placeholder':'Фамилия',
		'autocomplete':'off'
		}))


	password1 = forms.CharField(max_length = 100 , widget = forms.TextInput(attrs={
		'class':'input_field',
		'placeholder':'Пароль (не менее 8 чисел)',
		'type':'password',
		'autocomplete':'off'
		}))


	password2 = forms.CharField(max_length = 100 , widget = forms.TextInput(attrs={
		'class':'input_field',
		'placeholder':'Подтверждение пароля',
		'type':'password',
		'autocomplete':'off'
		}))


	class Meta:
		model = User
		fields = ['username','first_name' , 'last_name' , 'password1' , 'password2']

class auth_form(forms.Form):

	username = forms.CharField(max_length = 100 , widget = forms.TextInput(attrs={
		'class':'field',
		'placeholder':'Имя пользователя',
		'type':'text',
		'autocomplete':'off'
		}))

	password = forms.CharField(max_length = 100 , widget = forms.TextInput(attrs={
		'class':'field',
		'placeholder':'Пароль',
		'type':'password',
		'autocomplete':'off'
		}))

	class Meta:
		model = User
		fields = ['username' , 'password']


class change_password(forms.Form):

	username = forms.CharField(max_length = 250 , widget = forms.TextInput(attrs = {
		'placeholder':'Введите имя пользователя',
		'type':'text',
		'autocomplete':'off',
		'class':'input_field'
		}))

	#password = forms.CharField(max_length = 250 , widget = forms.PasswordInput(attrs = {
		#'placeholder':'Старый пароль',
		#'type':'password',
		#'autocomplete':'off',
		#'class':'input_field'
		#}))


	newpassword1 = forms.CharField(max_length = 250 , widget = forms.PasswordInput(attrs = {
		'placeholder':'Новый пароль(не менее 7 чесел и 1 буквы)',
		'type':'password',
		'autocomplete':'off',
		'class':'input_field'
		}))


	newpassword2 = forms.CharField(max_length = 250 , widget = forms.PasswordInput(attrs = {
		'placeholder':'Подтверждение нового пароля',
		'type':'password',
		"autocomplete":"off",
		'class':'input_field'
		}))


	class Meta:
		model = User
		fields = ['username','password' , 'newpassword1' , 'newpassword2']


class search_form(forms.Form):
	search = forms.CharField(max_length = 250 , widget = forms.TextInput(attrs = {
		'placeholder':'Поиск',
		'type':'text',
		'autocomplete':'off',
		'id':'search'
		}))


class message_form(ModelForm):
	message = forms.CharField(max_length = 250 , widget = forms.TextInput(attrs = {
		'placeholder':'Сообщение',
		'type':'text',
		'autocomplete':'off',
		})) 


	class Meta:
		model = message_model
		fields = ['message']