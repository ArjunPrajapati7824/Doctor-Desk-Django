# Generated by Django 4.2 on 2023-06-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0025_appointmentbookingform_appointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentbookingform',
            name='Appintment_Status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]