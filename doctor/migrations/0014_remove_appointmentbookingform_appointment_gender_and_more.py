# Generated by Django 4.2 on 2023-06-01 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0013_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentbookingform',
            name='Appointment_Gender',
        ),
        migrations.RemoveField(
            model_name='appointmentbookingform',
            name='Doctor_Name',
        ),
        migrations.RemoveField(
            model_name='appointmentbookingform',
            name='Doctor_id',
        ),
        migrations.AddField(
            model_name='appointmentbookingform',
            name='Appintment_Email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
