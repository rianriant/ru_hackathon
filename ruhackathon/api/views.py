from django.shortcuts import render
from rest_framework import generics
from main.models import Ivent
from .serializers import IventSerializer

class IventListCreateView(generics.ListCreateAPIView):
  queryset = Ivent.objects.all()
  serializer_class = IventSerializer    
