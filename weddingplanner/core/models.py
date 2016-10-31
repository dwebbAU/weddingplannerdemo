from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
	user = models.OneToOneField(User)
	
	def __str__(self):
		return self.user.username


class ServiceProvider(models.Model):
	user = models.OneToOneField(User)

	def __str__(self):
		return self.user.username

class Service(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class ServiceOffering(models.Model):
	service_provider = models.ForeignKey(ServiceProvider)
	service = models.ForeignKey(Service)
	cost = models.DecimalField(max_digits=6,decimal_places=2)

	def __str__(self):
		return self.service
