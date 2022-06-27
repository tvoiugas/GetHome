from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.forms import AuthenticationForm
from users.forms import RegistrationForm
from django.contrib.auth.decorators import login_required

def login_page(request):
	form = AuthenticationForm()
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			print("works")
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user) 
				return redirect('index')

	context = {
		'form': form
	}

	return render(request, 'users/login_page.html', context)


def logout_page(request):
	logout(request)
	return redirect('index')

def register_page(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')

	context = {'form': form}
	return render(request, 'users/register_page.html', context)

@login_required
def me(request):
	return render(request, 'users/me.html')
