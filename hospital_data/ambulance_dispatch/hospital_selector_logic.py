from geopy.distance import geodesic
from data_warehouse.models import Hospital

def calculate_distance(point1, point2):
    # Calculate distance between two GPS coordinates using geodesic distance
    return geodesic(point1, point2).kilometers

def choose_hospital(patient_data):
    severity = patient_data['severity']
    medical_condition = patient_data['medical_condition']
    patient_location = patient_data['location']

    # Retrieve hospitals based on the required facility and specialization
    if medical_condition == 'head trauma':
        hospitals = Hospital.objects.filter(facilities__icontains='neuro surgery')
    elif medical_condition == 'bone fracture':
        hospitals = Hospital.objects.filter(facilities__icontains='a&e')
    elif medical_condition == 'burn':
        hospitals = Hospital.objects.filter(facilities__icontains='burn unit')
    elif medical_condition == 'internal injury':
        hospitals = Hospital.objects.filter(facilities__icontains='operating theatres')
    else:
        hospitals = Hospital.objects.filter(facilities__icontains='a&e') # cahnge this


    # Initialize variables to track the best hospital
    best_hospital = None
    best_priority = 0
    best_distance = float('inf')

    for hospital in hospitals:
        # Calculate distance between patient and hospital
        distance = calculate_distance(patient_location, hospital.hospital_location)
        print(f'{distance} : {hospital.hospital_name}')
        # Calculate priority based on severity
        if severity == 'critical':
            priority = 4
        elif severity == 'serious':
            priority = 3
        elif severity == 'stable':
            priority = 2
        else:
            priority = 1

        # Update best hospital if conditions are met
        if priority > best_priority or (priority == best_priority and distance < best_distance):
            best_hospital = hospital
            best_priority = priority
            best_distance = distance
            

    if best_hospital:
        return best_hospital.hospital_name, float("{:.2f}".format(best_distance)), best_hospital.facilities
    else:
        return "No suitable hospital found"

# Example patient data
patient_data = {
    'severity': 'serious',
    'medical_condition': 'head',
    'location': (60.85, -5.25)  # Example GPS coordinates
}

chosen_hospital = choose_hospital(patient_data)
print("Chosen Hospital:", chosen_hospital)
