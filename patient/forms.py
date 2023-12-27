# from django import forms
# from .models import Patient_Registration

# class PatientForm(forms.ModelForm):
#     class Meta:
#         model = Patient_Registration
#         fields = ['PatientName', 'PatientPhoneNumber', 'PatientEmail', 'PatientGender', 'PatientAge', 'PatientPassword']

# from django import forms
# from django.contrib.auth.forms import *
# from django.contrib.auth.models import *
# from .models import *

# class PatientLoginform(UserCreationForm):
#     password2 = forms.CharField(label='confirm password(again)',widget=forms.PasswordInput)
#     class Meta:
#         model=PatientLoginForm
#         fields=['patientmobile','Patient_password']