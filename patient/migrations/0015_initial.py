# Generated by Django 4.2 on 2023-05-31 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0014_delete_patient_registration_delete_patientloginform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_Name', models.CharField(max_length=20)),
                ('Patient_PhoneNumber', models.CharField(max_length=10)),
                ('Patient_Email', models.EmailField(max_length=254)),
                ('Patient_Gender', models.CharField(max_length=10)),
                ('Patient_Age', models.IntegerField()),
                ('Patient_Password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PatientLoginForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientPhoneNumber', models.CharField(max_length=20)),
                ('PatientPassword', models.CharField(max_length=100)),
            ],
        ),
    ]
