from rest_framework import serializers
from tracker.models import Cylinder


class CylinderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cylinder
        fields = '__all__'
