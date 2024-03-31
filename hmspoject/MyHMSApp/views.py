from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Doctors, Patients, Appointment, Prescriptions
# from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate


@api_view()
def hello_world(request):
    return Response({"message": "Hello, World!"})

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def DoctorRecord(request, pk=None):
    try:
        if request.method == "GET":
            if pk is not None:
                try: 
                #retrive one Doctor id data
                    Get_one_ID = Doctors.objects.get(id=pk)
                    # Get_one_ID = Doctors.objects.filter(id=pk)
                    serializer = DoctorsSerializer(Get_one_ID, many=False)
                    return Response(serializer.data)
                except  Doctors.DoesNotExist:
                    return Response({"Messages": "data not found"})

            
                
            else:
                # retrive all Doctors id data
                Doct_Get = Doctors.objects.all()
                serializedData = DoctorsSerializer(Doct_Get, many=True)
                return Response({"Doct_Get": serializedData.data})
                # return Response({"Messages": "data not found"})
                
        
        elif request.method == "POST":
            # Add new doctors data
            jsonData = request.data
            # print(jsonData) output give in the form of json form
            serializedData = DoctorsSerializer(data=jsonData)
            if serializedData.is_valid():
                serializedData.save()
                return Response({"message": "data saved"})
            return Response({"message": "Invalid data"})
        #Delete Doctor Recore
        
        elif request.method == 'DELETE':
            doctor = Doctors.objects.get(id=pk)
            # doctor = Doctors.objects.filter(id=pk).first()
            if doctor:
                doctor.delete()
                return Response("Record deleted successfully")
            else:
                return Response({"message": "Doctor not found"})
    #update Doctor recode 
        elif request.method == 'PUT':
            doctor = Doctors.objects.get(id=pk)
            if doctor:
                serializer_update = DoctorsSerializer(instance=doctor, data=request.data)
                if serializer_update.is_valid():
                    serializer_update.save()
                    return Response({"message": "Data updated successfully"})
                return Response(serializer_update.errors)
            # else:
            #     return Response({"message": "Doctor not found"})
    except  Doctors.DoesNotExist:
                    return Response({"Messages": "data not found"})        

# ======================Patients =====================
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def PatientsRecord(request, pk=None):
    try:
        if request.method == "GET":
            if pk is not None: 
                try:
                # Retrieve one Patient id data
                    Get_one_ID = Patients.objects.get(id=pk)
                    serializer = PatientsSerializer(Get_one_ID, many=False)
                    return Response(serializer.data) 
                except  Patients.DoesNotExist:
                    return Response({"Messages": "data not found"})    
                
            else:
                # Retrieve all Patients id data
                Pati_Get = Patients.objects.all()
                serializedData = PatientsSerializer(Pati_Get, many=True)
                return Response({"Pati_Get": serializedData.data})
                
        elif request.method == "POST":
            # Add new Patients data
            jsonData = request.data
            serializedData = PatientsSerializer(data=jsonData)
            if serializedData.is_valid():
                serializedData.save()
                return Response({"message": "data saved"})
            return Response({"message": "Invalid data"})
        
        elif request.method == 'DELETE':
            # Delete Patients Record
            patient = Patients.objects.get(id=pk)
            
            if patient:
                patient.delete()
                return Response("Record deleted successfully")
            else:
                return Response({"message": "Patient not found"}, status=404)
        
        elif request.method == 'PUT':
            # Update Patients Record
            patient_instance = Patients.objects.get(id=pk)
            if patient_instance:
                serializer_update = PatientsSerializer(instance=patient_instance, data=request.data)
                if serializer_update.is_valid():
                    serializer_update.save()
                    return Response({"message": "Data updated successfully"})
                return Response({"message": "Data  not update"})
            # else:
            #     return Response({"message": "Patient not found"})
    except  Patients.DoesNotExist:
                    return Response({"Messages": "data not found"})
        
# ========================Appointment============
@api_view(['GET', 'POST'])
def AppointmentRecord(request, pk=None, doctor_id=None,patient_id=None):
    if request.method == "GET":
        if pk is not None: 
            # Retrieve one Appointment by appointment id
            appointment = get_object_or_404(Appointment, id=pk)
            serializer = AppointmentSerializer(appointment)
            return Response(serializer.data) 

        if doctor_id is not None:
            # Retrieve appointments for a specific doctor
            appointments = Appointment.objects.filter(Doctor_id=doctor_id)  # Use Doctor_id here
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data) 

        # patient_id = request.query_params.get('patient_id')
        if patient_id is not None:
            # Retrieve appointments for a specific patient
            appointments = Appointment.objects.filter(Patient_id=patient_id)  # Use Patient_id here
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data) 

        # If no specific criteria provided, return all appointments
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data) 
 
    
    
    elif request.method == "POST":
        # Add new Appointment data
        jsonData = request.data
        serializedData = AppointmentSerializer(data=jsonData)
        if serializedData.is_valid():
            serializedData.save()
            return Response({"message": "data saved"})
        return Response({"message": "Invalid data"})
    
    
# =====================prescriptions=============    
@api_view(['GET', 'POST'])
def PrescriptionsRecord(request, pk=None, doctor_id=None, patient_id=None):
    if request.method == "GET":
        if pk is not None: 
            # Retrieve one Prescription by prescription id
            prescription = get_object_or_404(Prescriptions, id=pk)
            serializer = PrescriptionsSerializer(prescription)
            return Response(serializer.data) 

        if doctor_id is not None:
            # Retrieve prescriptions for a specific doctor
            prescriptions = Prescriptions.objects.filter(Doctor_id=doctor_id)
            serializer = PrescriptionsSerializer(prescriptions, many=True)
            return Response(serializer.data) 

        if patient_id is not None:
            # Retrieve prescriptions for a specific patient
            prescriptions = Prescriptions.objects.filter(Patient_id=patient_id)
            serializer = PrescriptionsSerializer(prescriptions, many=True)
            return Response(serializer.data) 

        # If no specific criteria provided, return all prescriptions
        prescriptions = Prescriptions.objects.all()
        serializer = PrescriptionsSerializer(prescriptions, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        # Add new Prescription data
        jsonData = request.data
        serializedData = PrescriptionsSerializer(data=jsonData)
        if serializedData.is_valid():
            serializedData.save()
            return Response({"message": "data saved"})
        return Response({"message": "Invalid data"})

    
# ======================================================
# def login(request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             password = serializer.validated_data['password']
#             role = serializer.validated_data['role']
            
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 if role == "Doctors" and user.Doctors:
#                     print(role)
#                     return Response({"message": "Login successfully"})
#                 elif role == "Patients" and user.Patients:
#                     return Response({"message": "Login successful"})
#                 else:
#                     return Response("User not found")
#             else:
#                 return Response("User not found")
#         return Response({"message": "BAD_REQUEST"})   
# =====================LOGIN=============
@api_view(['POST'])    
def login(request):
    Email = request.data.get('Email')
    Password = request.data.get('Password')
    role = request.data.get('role')
      
    if role =="doctor":
        Doctor = Doctors.objects.filter(Email=Email, Password=Password)
        if Doctor.exists():
             return Response({"message":"Login successfully"})
        else:
             return Response({"message":" NOT Done Login "})
    elif role =="patient":
            Get_Patient = Patients.objects.filter(Email=Email, Password=Password)
            if Get_Patient.exists():
                 return Response({"message":" Patients Login successfully"})
            else:
                return Response({"message":" NOT exists Login "})
                      
    else:
        return Response({"message":" Invaild Role"})
                     
         
             
             
           