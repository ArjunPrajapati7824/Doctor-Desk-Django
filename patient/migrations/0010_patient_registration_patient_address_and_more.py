# Generated by Django 4.2 on 2023-05-30 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_remove_patient_registration_patient_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_registration',
            name='Patient_Address',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_registration',
            name='Patient_Age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_registration',
            name='Patient_Email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_registration',
            name='Patient_Gender',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_registration',
            name='Patient_Name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_registration',
            name='Patient_Password',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_registration',
            name='Patient_PhoneNumber',
            field=models.CharField(default=11, max_length=10),
            preserve_default=False,
        ),
    ]