from django.shortcuts import render

from core.models import Customer

def index(request):
	customers = Customer.objects.all()
	return render(request,'index.html',{'customers':customers})
