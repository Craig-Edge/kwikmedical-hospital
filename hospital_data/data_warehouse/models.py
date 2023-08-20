from django.db import models

class Hospital(models.Model):
    FACILITIES_CHOICES = (
        ('ICU', 'icu'),
        ('A&E', 'a&e'),
        ('Burn Unit', 'burn unit'),
        ('Operating Theatres', 'operating theatres'),
        ('Neuro Surgery', 'neuro surgery')
    )
    
    hospital_name = models.CharField(max_length=255, blank=False, null=False)
    hospital_location = models.CharField(max_length=100)
    facilities = models.CharField(max_length=255)
    
    def __str__(self):
        return self.hospital_name
