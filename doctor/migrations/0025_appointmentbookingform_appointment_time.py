# Generated by Django 4.2 on 2023-06-01 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0024_appointmentbookingform_appointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentbookingform',
            name='Appointment_time',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
