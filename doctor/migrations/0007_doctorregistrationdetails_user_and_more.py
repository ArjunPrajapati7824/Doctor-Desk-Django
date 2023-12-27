# Generated by Django 4.2 on 2023-05-30 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_patient_registration_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0006_alter_appointmentbookingform_doctor_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorregistrationdetails',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointmentbookingform',
            name='Doctor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctorregistrationdetails'),
        ),
        migrations.AlterField(
            model_name='appointmentbookingform',
            name='Patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient_registration'),
        ),
    ]