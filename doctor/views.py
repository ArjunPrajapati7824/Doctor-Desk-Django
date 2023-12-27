from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import *
from twilio.rest import Client
import os


from patient.models import Patient_Registration
# Create your views here.

def index(request):
    return redirect(reverse_lazy('login_doctor'))


def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def DoctorRegistration(request):
    if request.method == "POST":
       Doctor_Name = request.POST.get('name')
       Doctor_Phone_Number = request.POST.get('Phonenumber')
       Doctor_Email_id = request.POST.get('email')
       Clinic_Name = request.POST.get('clinic_name')
       Doctor_Clinic_Address = request.POST.get('city_Address')
       Doctor_Specialization=request.POST.get('specialization')
       Password = request.POST.get('password')
       Confirm_Password=request.POST.get('confirmpassword')
       doctor_register=DoctorRegistrationdetails(Doctor_Name=Doctor_Name,Doctor_Phone_Number=Doctor_Phone_Number,Doctor_Email_id=Doctor_Email_id,Clinic_Name=Clinic_Name,Doctor_Clinic_Address=Doctor_Clinic_Address,Doctor_Specialization=Doctor_Specialization,Password=Password,Confirm_Password=Confirm_Password)
       doctor_register.save() 
       return redirect(reverse_lazy('login_doctor'))
    return render(request,'Registration.html')

def DoctorHome(request):
    return render(request,'DoctorHome.html')

def DoctorAppointments(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        appointment = appointmentBookingForm.objects.get(id=appointment_id)
        contact_number = appointment.Appointment_Number
        appointment.delete()
        account_sid = "ACc121c24a356174a27a67056c85ae95e2"
        auth_token = "96770bb2506a1e363fe618d6d9fa6495"
        client = Client(account_sid, auth_token)

        message = client.messages \
                .create(
                     body="Sorry!,Your Appointment has been Rejected.",
                     from_='+14178043893',
                     to=f"+91{contact_number}")
        # messages.success(request, 'Your appointment has been declined.',extra_tags=contact_number)
    appointments=appointmentBookingForm.objects.all()
    return render(request,'DoctorAppointments.html',{"appointments":appointments})

def DoctorConfirmAppointments(request):
    
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        appointment_status = appointmentBookingForm.objects.get(id=appointment_id)
        contact_number = appointment_status.Appointment_Number
        appointment_status.Appintment_Status="Accept"
        appointment_status.save()
        account_sid = "ACc121c24a356174a27a67056c85ae95e2"
        auth_token = "96770bb2506a1e363fe618d6d9fa6495"
        client = Client(account_sid, auth_token)

        message = client.messages \
                .create(
                     body="Congratulations!,Your Appointment has been Accepted.",
                     from_='+14178043893',
                     to=f"+91{contact_number}")
        print("send")
        # messages.success(request, 'Your appointment has been Accepted.',extra_tags=contact_number)
    appointments=appointmentBookingForm.objects.all()
    return render(request,'DoctorConfirmAppointment.html',{"appointmentsconfirm":appointments})

def DoctorPatient(request):
    patients=Patient_Registration.objects.all()
    return render(request,'DoctorPatient.html',{"patients":patients})
       
# def delete_Appointment(request,id):
#     appointment=appointmentBookingForm.objects.get(id=id)
#     appointment.delete()
#     return render(request,"DoctorHome.html")

def DoctorLogin(request):
    doctor_id = request.session.get('loginiddr')
    if not doctor_id:
        if request.method == 'POST':
            Doctor_Phone_Number = request.POST.get('drPhonenumber')
            Password = request.POST.get('drpassword')
            try:
                doctor = DoctorRegistrationdetails.objects.get(Doctor_Phone_Number=Doctor_Phone_Number, Password=Password)
                request.session['loginiddr']=doctor.id
                if doctor is not None:
                    return redirect('home_doctor')
                else:
                    return render(request,'DoctorLogin.html',{'error':'Password does not match'})
                    # return redirect('login_doctor')
            except DoctorRegistrationdetails.DoesNotExist:
                return render(request,'DoctorLogin.html',{'error':'Password does not match'})
        return render(request,'DoctorLogin.html')
    return render(request,'DoctorHome.html')


def doctorLogout(request):
    logout(request)
    return redirect(reverse_lazy('login_doctor'))