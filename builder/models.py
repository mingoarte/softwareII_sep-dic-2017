from django.db import models
from django.contrib.auth.models import User
import os

def get_user_path(username):
	return os.path.join('uploads/templates', username)

class Template(models.Model):
	user = models.OneToOneField(User)
	html = models.FileField(upload_to='uploads/templates')
	created_at = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id)


class Pattern(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name


class Generic(models.Model):
	name = models.CharField(max_length=128)
	option1 = models.CharField(max_length=128, choices=(("Choice 1", "Choice 1"), ("Choice 2", "Choice 2")))
	option2 = models.CharField(max_length=128, choices=(("Choice 2.1", "Choice 2.1"), ("Choice 2.2", "Choice 2.2")))

	def __str__(self):
		return self.name
	

