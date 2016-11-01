from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from core.models import Customer, Event
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Customer

@login_required
def index(request):
    try:
      event = Event.objects.get(user=request.user)
    except Event.DoesNotExist:
      return redirect('setup')

    return redirect('dashboard')

@login_required
def setup(request):
    try:
      event = Event.objects.get(user=request.user)
    except Event.DoesNotExist:
      return render(request,'setup.html')

    return redirect('dashboard')

@login_required
def dashboard(request):
    try:
      event = Event.objects.get(user=request.user)
    except Event.DoesNotExist:
      return redirect('setup')

    return render(request,'dashboard.html')		
