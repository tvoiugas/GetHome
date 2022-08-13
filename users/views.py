import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from estates.models import Estate
from .tokens import account_activation_token
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


from .models import CustomUser
from .forms import CustomUserCreationForm




def login_page(request):
	form = AuthenticationForm()
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('index')
	return render(request, 'users/login_page.html', {'form': form})


@login_required
def logout_page(request):
	logout(request)
	return redirect('index')


def register_page(request):
	form = CustomUserCreationForm()
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect('index')

	context = {
		'form': form
	}
	return render(request, 'users/register_page.html', context)

def account_activation(request, uidb64, token):
	try:
		uid = force_str(urlsafe_base64_decode(uidb64))
		user = CustomUser.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
		user = None

	if user and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		return redirect('profile', userID=user.id)
	else:
		return render(request, 'users/activation_failed.html')

@login_required
def profile_page(request):
    # profile = get_object_or_404(CustomUser)
    estete = Estate.objects.all().filter(author=request.user)
   
    return render(request, 'users/profile.html', {'estate': estete})