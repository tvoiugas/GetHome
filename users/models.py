from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.core.mail import send_mail

from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('Имя'), max_length=20)
    last_name = models.CharField(_('Фамилия'), max_length=30)
    username = models.CharField(
        _('Имя пользователя'), max_length=20, unique=True)
    email = models.EmailField(_('Электронная почта'), unique=True)
    phone_number = PhoneNumberField(
        _('Номер телефона'), null=False, blank=False)
    birth_date = models.DateField(_('Дата рождения'))
    slug = models.CharField(max_length=20, default='')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_pro = models.BooleanField(default=False)
    limit = models.IntegerField(default=1, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email',
                       'phone_number', 'birth_date', 'is_staff',
                       'is_active', 'is_pro', 'limit']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(CustomUser, self).save(*args, **kwargs)


class Profile(models.Model):
    photo = models.ImageField(upload_to='users', null=True, blank=True)
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username
