# Generated by Django 4.2 on 2023-06-01 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0023_alter_appointmentbookingform_appointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentbookingform',
            name='Appointment_date',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
