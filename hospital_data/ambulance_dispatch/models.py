from django.db import models
from django.utils import timezone
from data_warehouse.models import Hospital

class DispatchRequest(models.Model):
    STATUS_CHOICES = [
        ('Accepted', 'accepted'),
        ('Denied', 'denied'),
        ('Requested', 'requested'),
        ('Ambulance Accepted', 'ambulance accepted')
    ]
    
    
    nhs_number = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)
    chosen_hospital = models.CharField(max_length=200)
    medical_condition = models.CharField(max_length=200, null=True)
    dispatch_status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='requested')

    def __str__(self):
        return f"Dispatch Request for NHS Number: {self.nhs_number}"
