from django.shortcuts import render
from core.models import Customer, ServiceProvider, Service, ServiceOffering, Event, ServiceRequirement
from rest_framework import generics
from api.serializers import CustomerSerializer, ServiceProviderSerializer, ServiceSerializer, ServiceOfferingSerializer, EventSerializer, ServiceRequirementSerializer

class CustomerList(generics.ListCreateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class ServiceProviderList(generics.ListCreateAPIView):
	queryset = ServiceProvider.objects.all()
	serializer_class = ServiceProviderSerializer

class ServiceProviderDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ServiceProvider.objects.all()
	serializer_class = ServiceProviderSerializer

class ServiceList(generics.ListCreateAPIView):
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer

class ServiceOfferingList(generics.ListCreateAPIView):
	queryset = ServiceOffering.objects.all()
	serializer_class = ServiceOfferingSerializer

	def get_queryset(self):
	  queryset = ServiceOffering.objects.all()
	  service = self.request.query_params.get('service',None)
	  if service is not None:
	    queryset = queryset.filter(service=service)
	  return queryset

class ServiceOfferingDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ServiceOffering.objects.all()
	serializer_class = ServiceOfferingSerializer

class EventList(generics.ListCreateAPIView):
	serializer_class = EventSerializer

	def get_queryset(self):
		user = self.request.user
		return Event.objects.filter(user=user)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer

class ServiceRequirementList(generics.ListCreateAPIView):
	serializer_class = ServiceRequirementSerializer
	
	def get_queryset(self):
		user = self.request.user
		return ServiceRequirement.objects.filter(event__user=user)

	def perform_create(self,serializer):
		user = self.request.user
		event = Event.objects.get(user=user)
		serializer.save(event=event)

class ServiceRequirementDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ServiceRequirement.objects.all()
	serializer_class = ServiceRequirementSerializer


