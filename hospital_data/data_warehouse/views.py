from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.response import Response
from .models import Hospital
from .serializers import HospitalSerializer
# Create your views here.

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    queryset = queryset.order_by('hospital_name')
    
    def get_querset(self):
        queryset = Hospital.objects.all()
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)