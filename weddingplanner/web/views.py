from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Customer

@login_required
def index(request):
	customers = Customer.objects.all()
	return render(request,'index.html',{'customers':customers})
