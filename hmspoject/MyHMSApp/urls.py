from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),
    path('doctors/',views.DoctorRecord),
    path('doctors/<int:pk>/',views.DoctorRecord),
    path('patients/',views.PatientsRecord),
    path('patients/<int:pk>/',views.PatientsRecord),
    path('appointment/',views.AppointmentRecord),
    path('appointment/<int:pk>/',views.AppointmentRecord),
    # path('appointments/?doctor_id=<doctor_id>',views.AppointmentRecord),
    path('appointments/doctor/<int:doctor_id>/', views.AppointmentRecord),
    path('appointments/patient/<int:patient_id>/', views.AppointmentRecord),
    path('Prescriptions/', views.PrescriptionsRecord),
    path('Prescriptions/<int:pk>/', views.PrescriptionsRecord),
    path('Prescriptions/doctor/<int:doctor_id>/', views.PrescriptionsRecord),
    path('Prescriptions/patient/<int:patient_id>/', views.PrescriptionsRecord),
    path('login/',views.login ,name='login'),
]