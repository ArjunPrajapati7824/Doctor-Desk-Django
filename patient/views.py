from datetime import timezone
from telnetlib import LOGOUT
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import *
from django.template import loader
from doctor.models import *
# from .forms import PatientForm

from .models import *
# Create your views here.

count9=0
count4=0

def index(request):
    return render(request,'PatientRegistration.html')

def patientHome(request):
    doctor = DoctorRegistrationdetails.objects.get(id=1)
    return render(request,'patientHome.html',{"doc":doctor})

def PatientRegistration(request):
    if request.method == "POST":
       Patient_PhoneNumber = request.POST.get('Phonenumber')
       try:
           pat = Patient_Registration.objects.get(Patient_PhoneNumber=Patient_PhoneNumber )
        #    print("==============",pat)
        #    print(isinstance(pat, str))
           if isinstance(pat,str):
               Patient_Name = request.POST.get('name')
               Patient_PhoneNumber = request.POST.get('Phonenumber')
               Patient_Email = request.POST.get('email')
               Patient_Gender = request.POST.get('gender')
               Patient_Age = request.POST.get('age')
               Patient_Password=request.POST.get('password')
               patient_register=Patient_Registration(Patient_Name=Patient_Name,Patient_PhoneNumber=Patient_PhoneNumber,Patient_Email=Patient_Email,Patient_Gender=Patient_Gender,Patient_Age=Patient_Age,Patient_Password=Patient_Password)
               patient_register.save()
               return redirect(reverse_lazy('patient_login'))
           else:
               messages.success(request,f'Already Exists') 
               
       except Patient_Registration.DoesNotExist:
           Patient_Name = request.POST.get('name')
           Patient_PhoneNumber = request.POST.get('Phonenumber')
           Patient_Email = request.POST.get('email')
           Patient_Gender = request.POST.get('gender')
           Patient_Age = request.POST.get('age')
           Patient_Password=request.POST.get('password')
           patient_register=Patient_Registration(Patient_Name=Patient_Name,Patient_PhoneNumber=Patient_PhoneNumber,Patient_Email=Patient_Email,Patient_Gender=Patient_Gender,Patient_Age=Patient_Age,Patient_Password=Patient_Password)
           patient_register.save()
           return redirect(reverse_lazy('patient_login'))


    return render(request,'PatientRegistration.html')

   
   
def PatientLogin(request):
    doctor = DoctorRegistrationdetails.objects.get(id=1)
    user_id=request.session.get('loginid')
    if not user_id:
        if request.method == 'POST':
                Patient_PhoneNumber = request.POST.get('Phonenumber')
                Patient_Password = request.POST.get('password')
                try: 
                    patient = Patient_Registration.objects.get(Patient_PhoneNumber=Patient_PhoneNumber, Patient_Password=Patient_Password) 
                    request.session['loginid']=patient.id
                    request.session['loginname']=patient.Patient_Name
                    if patient is not None:
                        messages.success(request,f'You are login Successfully!')
                        return render(request,'patientHome.html',{'userobj':patient,"doc":doctor})
                except Patient_Registration.DoesNotExist:
                    error_message = 'Invalid mobile number or password.'
                    return render(request, 'patientLogin.html', {'error_message': error_message})
            
        return render(request,'patientLogin.html')
    return redirect(reverse_lazy('Patienthome'))
    
def bookDoctors(request):
    doctors=DoctorRegistrationdetails.objects.all()
    return render(request,'DoctorBooking.html',{'doctors':doctors})
   
def bookAppointment(request,id):
    # count=0
    user=Patient_Registration.objects.get(id=id)
    # P_id=Patient_Registration.objects.get(id=id)
    
    if request.method == "POST":
    #    Patient_id = P_id.id
       Appointment_Name = request.POST.get('patientName')
       Appointment_Number = request.POST.get('contactNumber')
       Appointment_Age = request.POST.get('patientAge')
       Appintment_Gender = request.POST.get('patientGender')
       Appointment_Description=request.POST.get('diseases')
       Appointment_date=request.POST.get('appointment_date')
       print("DAteeeeeeeeeee",Appointment_date)
       Appointment_time=request.POST.get('timeSlot')
       Appintment_Status=request.POST='Pending'
       big=datetime.today().year,"-",datetime.today().month,"-",datetime.today().day           
       if (Appointment_date>str(big)):
           appointment_book=appointmentBookingForm(Appointment_Name=Appointment_Name,Appointment_Number=Appointment_Number,Appointment_Age=Appointment_Age,Appintment_Gender=Appintment_Gender,Appointment_Description=Appointment_Description,Appointment_date=Appointment_date,Appointment_time=Appointment_time,Appintment_Status=Appintment_Status)
           appointment_book.save()
       else:
           messages.success(request,f'datee')
           
    #    if (timezone.now()<=Appointment_date):
    #         
    #    else:
       
           
           
            
       
    #    global count9
    #    global count4
    #    if Appointment_time=='9-12':
    #        count9+=1
    #    if Appointment_time=='4-7':
    #        count4+=1
    #    print(count)
       messages.success(request,f'Your appointment has been booked Wait for confirmation')
       return redirect(reverse_lazy('Patienthome'))   
    return render(request,'appointmentBookingForm.html',{'patient':user})
    # return render(request,'appointmentBookingForm.html',{'patient':user,"count9":count9,"count4":count4})

def patientLogout(request):
    logout(request)
    return redirect(reverse_lazy('patient_login'))

def patientProfile(request,id):
    users=Patient_Registration.objects.get(id=id)
    return render(request,'patientProfile.html',{'users':users})


def update_Patient_Recored(request,id):
    Patient_Name=request.POST.get('uname')
    Patient_Age=request.POST.get('uage')
    Patient_Email=request.POST.get('uemail')
    Patient_PhoneNumber=request.POST.get('uphone')

    patient = Patient_Registration.objects.get(id=id)
    patient.Patient_Name = Patient_Name
    patient.Patient_Age = Patient_Age
    patient.Patient_Email = Patient_Email
    patient.Patient_PhoneNumber = Patient_PhoneNumber
    patient.save()
    return redirect(reverse_lazy('Patienthome'))