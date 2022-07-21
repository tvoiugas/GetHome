from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, first_name, last_name, username, email, phone_number, birth_date, password, **extra_fields):
        # Create and save user
        if not username:
            raise ValueError(_('Вы должны указать имя пользователя'))

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, username=username,
                          email=email, phone_number=phone_number, birth_date=birth_date, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, username, email, phone_number, birth_date, password, **extra_fields):

        # Create and save superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_pro', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                _('Супер пользователь должен иметь is_stuff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                _('Супер пользователь должен иметь is_superuser=True.'))
        if extra_fields.get('is_pro') is not True:
            raise ValueError(
                _('Супер пользователь должен иметь is_ispro=True.'))
        return self.create_user(first_name, last_name, username, email, phone_number, birth_date, password, **extra_fields)
