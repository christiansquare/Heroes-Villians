from rest_framework import serializer
from .models import super_types

class Super_typesSerializer(serializer.ModelSerializer):
    class Meta:
        model = super_types
        fields = ['id','types']