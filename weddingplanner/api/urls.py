from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
	url(r'^customers/$',views.CustomerList.as_view()),
	url(r'^customer/(?P<pk>[0-9]+)/$',views.CustomerDetail.as_view()),
	url(r'^serviceproviders/$',views.ServiceProviderList.as_view()),
	url(r'^serviceprovider/(?P<pk>[0-9]+)/$',views.ServiceProviderDetail.as_view()),
	url(r'^services/$',views.ServiceList.as_view()),
	url(r'^service/(?P<pk>[0-9]+)/$',views.ServiceDetail.as_view()),
	url(r'^serviceofferings/$',views.ServiceOfferingList.as_view()),
	url(r'^serviceoffering/(?P<pk>[0-9]+)/$',views.ServiceOfferingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
