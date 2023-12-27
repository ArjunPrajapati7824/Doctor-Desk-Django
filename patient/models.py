from django.db import models


# Create your models here.

class Patient_Registration(models.Model):
    Patient_Name=models.CharField(max_length=20)
    Patient_PhoneNumber=models.CharField(max_length=10)
    Patient_Email=models.EmailField()
    Patient_Gender=models.CharField(max_length=10)
    Patient_Age=models.IntegerField()
    Patient_Password=models.CharField(max_length=10)   

    
    def __str__(self):
        return self.Patient_Name
    

class PatientLoginForm(models.Model):
    PatientPhoneNumber = models.CharField(max_length=20)
    PatientPassword = models.CharField(max_length=100)




