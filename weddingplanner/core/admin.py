from django.contrib import admin
from .models import Customer, ServiceProvider, Service, ServiceOffering, Event, ServiceRequirement

# Register your models here.
admin.site.register(Customer)
admin.site.register(ServiceProvider)
admin.site.register(Service)
admin.site.register(ServiceOffering)
admin.site.register(Event)
admin.site.register(ServiceRequirement)
