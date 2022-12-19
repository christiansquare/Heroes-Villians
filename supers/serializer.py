from rest_framework import serializers
from .models import Supers

class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['id','name','alter_ego','secondary_ability','catchphrase','super_type']
        depth = 1