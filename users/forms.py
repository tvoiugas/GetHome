from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from django import forms

from .models import CustomUser
# , Profile


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'username', 'email',
            'phone_number', 'birth_date', 
            # 'is_staff', 'is_active',
            # 'limit', 'is_pro',
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'username', 'email',
            'phone_number', 'birth_date',
            #  'is_staff', 'is_active',
            # 'limit', 'is_pro',
        )


# class ProfileForm(forms.ModelForm):

#     class Meta:
#         model = Profile
#         fields = (
#             'photo',
#         )
