from rest_framework import serializers
from .models import *


class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = "__all__"
        
        
        
class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = "__all__"        
        
        
        
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"        

class PrescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescriptions
        fields = "__all__"                        
        
        
        
# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()
#     role = serializers.CharField()        