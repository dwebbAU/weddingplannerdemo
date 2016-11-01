<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from core.models import Customer, Event
=======
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Customer
>>>>>>> df781d7c097d38597f6f9db0058aae4b23ad12e5

@login_required
def index(request):
    try:
      event = Event.objects.get(user=request.user)
    except Event.DoesNotExist:
      return redirect('setup')

    return redirect('dashboard')

@login_required
def setup(request):
	return render(request,'setup.html')

@login_required
def dashboard(request):
	return render(request,'setup.html')		
