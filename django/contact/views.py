from django.shortcuts import render
from .models import Contact_info
from .serializers import Contact_info_serializer
from rest_framework import viewsets

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact_info.objects.all()
    serializer_class = Contact_info_serializer