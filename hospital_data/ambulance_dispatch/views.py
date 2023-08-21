# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from data_warehouse.models import Hospital 
from .models import DispatchRequest
from .serializers import DispatchRequestSerializer
from .hospital_selector_logic import choose_hospital
from datetime import datetime

class AmbulanceDispatchViewSet(viewsets.ViewSet):
    def create(self, request):
        nhs_number = request.data.get('nhs_number')
        location = request.data.get('location')
        severity = request.data.get('severity')
        medical_condition = request.data.get('medical_condition')
        
        patient_data = {
            'severity': severity,
            'medical_condition': medical_condition,
            'location': location,
        }
        
        response_data = choose_hospital(patient_data)
        
        current_datetime = datetime.now()
        current_date = current_datetime.date()
        current_time = current_datetime.time()

        chosen_hospital_name = response_data[0]
        chosen_hospital = Hospital.objects.get(hospital_name=chosen_hospital_name)
        dispatch_request = DispatchRequest.objects.create(
            nhs_number=nhs_number,
            location=location,
            chosen_hospital=chosen_hospital, 
            medical_condition=medical_condition,
            datetime=current_datetime,
            date=current_date,
            time=current_time
        )

        serializer = DispatchRequestSerializer(dispatch_request)

        return Response({
            'chosen_hospital': response_data[0],
            'distance': response_data[1],
            'facilities': response_data[2],
            'dispatch_request': serializer.data,
            'medical_condition': medical_condition,
            'date': dispatch_request.date,
            'time': dispatch_request.time
        })


class DispatchRequestViewSet(viewsets.ModelViewSet):
    queryset = DispatchRequest.objects.all()
    serializer_class = DispatchRequestSerializer  
    def get_queryset(self):
        queryset = DispatchRequest.objects.all()
        hospital = self.request.query_params.get('hospital_name')
        dispatch_status = self.request.query_params.get('dispatch_status')
        queryset = queryset.order_by('datetime')
        if hospital:
            queryset = self.queryset.filter(chosen_hospital=hospital)
        if dispatch_status:
            queryset = self.queryset.filter(dispatch_status=dispatch_status)
            return queryset
        return queryset

    def partial_update(self, request, pk=None, *args, **kwargs):
        print('inside partial_update')
        instance = self.get_object()
        print(f'request : {request.data}')
        dispatch_status = request.data.get('dispatch_status')
        print(f'dispatch_status {dispatch_status}')
        if dispatch_status is not None:
            instance.dispatch_status = dispatch_status
            instance.save()
            return Response({'dispatch_status': dispatch_status})
        else:
            return Response({'detail': 'dispatch_status field is required.'}, status=400)