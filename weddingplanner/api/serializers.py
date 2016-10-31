from rest_framework import serializers
from core.models import Customer, ServiceProvider, Service, ServiceOffering

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = ('user',)

class ServiceProviderSerializer(serializers.ModelSerializer):
	class Meta:
		model = ServiceProvider
		fields = ('user',)

class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = ('name',)

class ServiceOfferingSerializer(serializers.ModelSerializer):
	class Meta:
		model = ServiceOffering
		fields = ('name','service_provider','cost')
