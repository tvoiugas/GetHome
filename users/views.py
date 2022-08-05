import re
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


from .models import CustomUser, Profile
from .forms import CustomUserCreationForm, ProfileForm


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
    if request.user.is_authenticated:
        return redirect('index')
    form = CustomUserCreationForm()
    form_profile = ProfileForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        form_profile = ProfileForm(request.POST)
        if form.is_valid() and form_profile.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()

            current_site = get_current_site(request)
            subject = 'Активация'
            message = render_to_string('users/activation_page.html', {
                'user': user, 'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })
            user.email_user(subject=subject, message=message)
            return redirect('index')
    context = {
        'form': form,
        'profile': form_profile
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
    profile = Profile.objects.get(user= request.user)
    return render(request, 'users/profile.html', {'profile': profile})
