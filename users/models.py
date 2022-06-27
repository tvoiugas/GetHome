from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	birth_date = models.DateField()
	bio = models.TextField()
	user = models.OneToOneField(User, on_delete=models.CASCADE)



	def __str__(self):
		return self.user.username
# Create your models here.
