from django.shortcuts import render
from django.http import HttpResponseRedirect , HttpResponse
from .forms import *
from django.contrib.auth.models import User
from django.contrib import auth 

print("------------------------------------")
print("| HELLO WORLD")
print("------------------------------------")

def reg_view(request): # Регистрация

	form = registr_form()

	if request.method == 'POST':
		form = registr_form(request.POST)

		if form.is_valid:
			password1 = request.POST.get('password1')
			password2 = request.POST.get('password2')

			if not password1 == password2:
				return render(request , 'error/error_registration.html', {'form':form})

			form.save()

			susername = form.cleaned_data['username']
			sfirst_name = form.cleaned_data['first_name']
			slast_name = form.cleaned_data['last_name']
			spassword = form.cleaned_data['password1']

			return HttpResponseRedirect('/')


	return render(request , 'reg/index.html' , {'form':form})



def auth_view(request): # Аутентификация

	form = auth_form()
	
	if request.method == 'POST':
		
		form = auth_form(request.POST)

		if form.is_valid:
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = auth.authenticate(username = username , password = password) 

			if user is not None:
				if user.is_active:
					auth.login(request, user)
					return HttpResponseRedirect('/account')


	return render(request , 'auth/index.html' , {'form':form})



def home_view(request): # HOME_PAGE
	if not request.user.is_authenticated:

		return render(request , 'error/error_account.html')


	return render(request , 'account/index.html')



def settings_view(request):

	if not request.user.is_authenticated:
		return render(request , 'error/error_account.html')


	return render(request , 'settings/index.html')



def change_password_view(request): #Смена пароля

	if not request.user.is_authenticated:
		return render(request , 'error/error_account.html')

	forma = change_password()

	if request.method == 'POST':
		forma = change_password(request.POST)

		if forma.is_valid:
			username = request.POST.get('username')
			newpassword1 = request.POST.get('newpassword1')
			newpassword2 = request.POST.get('newpassword2')

			u = User.objects.get(username = username)

			if not newpassword1 == newpassword2:
				return render(request , 'error_change_password.html' , {'forma':forma})

			u.set_password(newpassword1)
			u.save()

			return HttpResponseRedirect('/account/logout')

	return render(request , 'change_password/index.html' , {'forma':forma})



def logout_view(request):
	if request.method == 'GET':
		auth.logout(request)


		return HttpResponseRedirect('/')


		
###class change_full_name(forms.Form):
###
###
###
###


def search_view(request):

	forma = search_form()

	if request.method == 'GET':
		forma = search_form(request.GET)
		if forma.is_valid:
			pass

			
	return render(request , 'search/index.html' , {'forma':forma})



def message_view(request):
	forma = message_form()
	model = message_model.objects.all()


	data = {
		'model':model,
		'forma':forma
	}


	if not request.user.is_authenticated:
		return HttpResponse(status = 404)

	if request.method == 'POST':
		forma = message_form(request.POST)

		if forma.is_valid:
			forma.save()

			return HttpResponseRedirect('/account/message')

	return render(request , 'message/index.html' , data)
