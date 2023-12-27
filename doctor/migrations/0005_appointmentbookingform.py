# Generated by Django 4.2 on 2023-05-27 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_doctorloginform'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointmentBookingForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctor_id', models.IntegerField(max_length=20)),
                ('Patient_id', models.IntegerField(max_length=20)),
                ('Doctor_Name', models.CharField(max_length=20)),
                ('Appointment_Name', models.CharField(max_length=20)),
                ('Appointment_Number', models.CharField(max_length=100)),
                ('Appointment_Age', models.CharField(max_length=100)),
                ('Appointment_Gender', models.CharField(max_length=100)),
                ('Appointment_Description', models.CharField(max_length=100)),
            ],
        ),
    ]
