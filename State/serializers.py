from rest_framework import serializers
from .models import StateModel

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateModel
        fields = '__all__'