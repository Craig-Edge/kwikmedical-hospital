from rest_framework import serializers
from .models import DispatchRequest

class DispatchRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchRequest
        fields = '__all__'
