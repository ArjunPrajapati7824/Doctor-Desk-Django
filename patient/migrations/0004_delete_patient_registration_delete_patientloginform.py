# Generated by Django 4.2 on 2023-05-27 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_rename_patientpassword_patient_registration_patient_password_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Patient_Registration',
        ),
        migrations.DeleteModel(
            name='PatientLoginForm',
        ),
    ]
