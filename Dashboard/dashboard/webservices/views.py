from django.shortcuts import render
from myapp.models import *
from .serializer import *
from rest_framework import viewsets
from django.contrib.auth.models import User

# Create your views here.


class account_viewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = account_serializer

class user_profile_viewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = user_profile_serializer

class document_viewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = document_serializer

class mander_viewset(viewsets.ModelViewSet):
    queryset = Mander.objects.all()
    serializer_class = mander_serializer

class service_viewset(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = service_serializer

class request_viewset(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = request_serializer

class request_manager_viewset(viewsets.ModelViewSet):
    queryset = Requestmanager.objects.all()
    serializer_class = request_manager_serializer

class vehicle_viewset(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()    
    serializer_class = vehicle_serializer



