from .models import Contact_info
from rest_framework import serializers


class Contact_info_serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_info
        fields = ('name', 'mobile_number', 'country', 'city' )