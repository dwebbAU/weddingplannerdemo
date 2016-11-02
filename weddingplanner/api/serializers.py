from rest_framework import serializers
from core.models import Customer, ServiceProvider, Service, ServiceOffering, Event, ServiceRequirement

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
		fields = ('name','pk')

class ServiceOfferingSerializer(serializers.ModelSerializer):
	service_name = serializers.CharField(source="service.name",read_only=True)
	service_provider_name = serializers.CharField(source="service_provider.user.username",read_only=True)
	
	
	class Meta:
		model = ServiceOffering
		fields = ('service','service_provider','cost','service_name','service_provider_name')

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = ('name','budget','location_lat','location_lon','pk')

class ServiceRequirementSerializer(serializers.ModelSerializer):
	service_name = serializers.CharField(source="service.name",read_only=True)
	service_icon = serializers.CharField(source="service.icon",read_only=True)

	class Meta:
		model = ServiceRequirement
		fields = ('service','service_name','service_icon')
