# Generated by Django 4.2 on 2023-05-31 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0012_remove_patient_registration_patient_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_registration',
            name='Patient_Password',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]