from django.conf.urls import url
from web import views

urlpatterns = [
	url(r'^$',views.index),	
	url(r'^setup/$',views.setup,name='setup'),
	url(r'^dashboard/$',views.dashboard,name='dashboard'),
]

