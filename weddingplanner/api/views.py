from django.shortcuts import render
from core.models import Customer, ServiceProvider, Service, ServiceOffering, Event
from rest_framework import generics
from api.serializers import CustomerSerializer, ServiceProviderSerializer, ServiceSerializer, ServiceOfferingSerializer, EventSerializer

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

class ServiceOfferingDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ServiceOffering.objects.all()
	serializer_class = ServiceOfferingSerializer

class EventList(generics.ListCreateAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
