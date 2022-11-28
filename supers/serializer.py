from rest_framework import serializer
from .models import Supers

class SupersSerializer(serializer.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['id','name','alter_ego','secondary_ability','catchphrase','super_type']
        depth = 1