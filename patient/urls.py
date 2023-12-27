from django.urls import path

from .views import *
urlpatterns = [

    path('',index,name="index"),
    path('patientregistration/',PatientRegistration,name="patient_registration"),
    path('patientLogin/',PatientLogin,name="patient_login"),
    path('Patienthome/',patientHome,name="Patienthome"),
    path('patientProfile/<int:id>',patientProfile,name="patientProfile"),
    path('patientLogout/',patientLogout,name="patientLogout"),
    # path('DoctorBooking/',bookDoctors,name="DoctorBooking"),
    path('BookAppointment/<int:id>',bookAppointment,name="BookAppointment"),
    path('patientProfile/updateDetail/<int:id>',update_Patient_Recored,name="updateDetail"),
   
]