# Generated by Django 4.2 on 2023-05-30 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_remove_patient_registration_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_registration',
            name='Patient_Address',
            field=models.CharField(default='', max_length=50),
        ),
    ]
