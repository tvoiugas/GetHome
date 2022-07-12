from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import RegistrationForm, ProfileForm

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

def profile_page(request, userID):
	profile = Profile.objects.get(user = userID)

	context = {
		'profile': profile
	}

	return render(request, 'users/profile.html', context)

def profile_create(request, userID):
	if request.POST:
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			form.instance.user = request.user
			form.save()
			return redirect('profile_page', pk = userID)
	else:
		form = ProfileForm()

	context = {
		'form': form
	}

	return render(request, 'users/profile_create.html', context)