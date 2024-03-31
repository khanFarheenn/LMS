from django.db import models

# =================Doctors class=================
class Doctors(models.Model):
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255) 
    Gender = models.CharField(max_length=255)
    Email = models.CharField(max_length=255 ,unique= True)
    Phone_Number = models.BigIntegerField()
    Password = models.CharField(max_length=255)

# =================Patients class=================
class Patients(models.Model):
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=255)
    Weight = models.CharField(max_length=255)
    Email = models.CharField(max_length=255,unique= True)
    Phone_Number = models.BigIntegerField()
    Password = models.CharField(max_length=255)

# ==================Appointments=================  
class Appointment(models.Model):
    Patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    Doctor= models.ForeignKey(Doctors, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

# ==================Prescriptions=================  
class Prescriptions(models.Model):
    Patient= models.ForeignKey(Patients, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    Medicine = models.CharField(max_length=255)
    Date_created = models.DateField(auto_now=True)  
