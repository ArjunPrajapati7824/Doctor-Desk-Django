from django.db import models
from datetime import datetime


# Create your models here.

class DoctorRegistrationdetails(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    Doctor_Name = models.CharField(max_length=1000, default="")
    Doctor_Phone_Number = models.IntegerField()
    Doctor_Email_id =models.EmailField()
    Doctor_Clinic_Address =models.CharField(max_length=10, default="")
    Clinic_Name = models.CharField(max_length=10, default="")
    Doctor_Specialization = models.CharField(max_length=10, default="")
    Password = models.CharField(max_length=10, default="")
    Confirm_Password = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.Doctor_Name
    

class DoctorLoginForm(models.Model):
    DoctorPhoneNumber = models.CharField(max_length=20)
    DoctorPassword = models.CharField(max_length=100)

       

class appointmentBookingForm(models.Model):
    Appointment_Name = models.CharField(max_length=20)
    Appointment_Number = models.CharField(max_length=100)
    Appointment_Age = models.CharField(max_length=100)
    Appintment_Gender = models.CharField(max_length=100)
    Appointment_Description = models.CharField(max_length=100)
    Appointment_date = models.CharField(max_length=100)
    Appointment_time = models.CharField(max_length=100)
    Appintment_Status=models.CharField(max_length=100)
  
    # Appointment_time = models.TimeField()

    # def str_to_date(value):
    #  if isinstance(value, datetime):
    #      return value.date()
    #  elif isinstance(value, str):
    #      try:
    #          return datetime.strptime(value, '%Y-%m-%d').date()
    #      except ValueError:
    #          raise ValueError('Invalid date string format. Expected format: YYYY-MM-DD')
        
    #  else:
    #      raise ValueError('Invalid input type. Expected str or datetime.')  

    
    # def save(self, *args, **kwargs):
    #     # Convert appointment_date and appointment_time to datetime objects
    #     if isinstance(self.appointment_date, str):
    #         self.appointment_date = str_to_date(self.appointment_date)
    #     if isinstance(self.appointment_time, str):
    #         self.appointment_time = datetime.strptime(self.appointment_time, '%H:%M').time()

    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.Appointment_Name
