from django.urls import path

from .views import *
urlpatterns = [

    path('',index,name="index_doctor"),
    #  path('registerdoctor',DoctorRegistration,name="register_doctor"),
    path('home/',DoctorHome,name="home_doctor"),
    # path('servicedoctor/',service,name="service_doctor"),
    path('logindoctor/',DoctorLogin,name="login_doctor"),
    path('doctorappointments/',DoctorAppointments,name="doctorappointments"),
    path('doctorconfirmappointments/',DoctorConfirmAppointments,name="doctorconfirmappointments"),
    path('doctorpatient/',DoctorPatient,name="doctorpatient"),
    path('doctorLogout/',doctorLogout,name="doctorLogout"),
   

]