# Generated by Django 4.2 on 2023-05-31 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_alter_appointmentbookingform_doctor_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorregistrationdetails',
            name='Doctor_Phone_Number',
            field=models.IntegerField(),
        ),
    ]