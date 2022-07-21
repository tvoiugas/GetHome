from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = (
        (
            "Fields",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone_number",
                    "email",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_pro",
                    "limit",
                    "password",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
