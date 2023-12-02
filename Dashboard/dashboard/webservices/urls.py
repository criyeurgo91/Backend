from django.urls import path, include
from rest_framework import routers
from myapp.models import *
from webservices.views import *

router = routers.DefaultRouter()
router.register(r'account', account_viewset)
router.register(r'user_profile', user_profile_viewset)
router.register(r'document', document_viewset)
router.register(r'mander', mander_viewset)
router.register(r'service', service_viewset)
router.register(r'request', request_viewset)
router.register(r'request_manager', request_manager_viewset)
router.register(r'vehicle', vehicle_viewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace= 'rest_framework')),
]