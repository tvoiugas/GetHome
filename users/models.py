from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	photo = models.ImageField(upload_to = 'users')
	birth_date = models.DateField()
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')


	class Meta:
		verbose_name = 'Profile'
		verbose_name_plural = 'Profiles'


	def __str__(self):
		return self.user.username