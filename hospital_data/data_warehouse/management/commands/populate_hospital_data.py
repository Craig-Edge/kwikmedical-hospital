import random
from itertools import cycle
from django.core.management.base import BaseCommand
from data_warehouse.models import Hospital


# List of hospital names
hospital_names = [
    "Starship Hospital", "Enterprise Medical Center", "Voyager General", "Defiant Healthcare",
    "Galactica Clinic", "Millennium Health Center", "Nebula Medical", "Pegasus Hospital",
    "Prometheus Medical Center", "Discovery Care", "Falcon Healthcare", "Serenity General",
    "USS Hospital", "Atlantis Medical Center", "Eagle Health Services", "Phoenix Clinic",
    "Rocinante Hospital", "Tardis Medical", "Stargate General", "Normandy Care"
]

# List of facilities
FACILITIES = [
    'ICU', 'A&E', 'Burn Unit', 'Operating Theatres', 'Neuro Surgery'
]

def generate_random_coordinates():
    # Generate random latitude and longitude within the specified range
    latitude = random.uniform(55.8, 56.1)  # Latitude range for central belt of Scotland
    longitude = random.uniform(-3.9, -4.4)  # Longitude range for central belt of Scotland
    return f"{latitude},{longitude}"  

class Command(BaseCommand):
    help = 'Populate the hospital database with sample data'

    def handle(self, *args, **options):
        Hospital.objects.all().delete()

        facility_cycle = cycle(FACILITIES) 

        # Loop to create hospitals
        for hospital_name in hospital_names:
            facility = next(facility_cycle)  
            hospital_location = generate_random_coordinates()  

            # Create the hospital record
            Hospital.objects.create(
                hospital_name=hospital_name,
                facilities=facility,
                hospital_location=hospital_location
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated hospital data'))
