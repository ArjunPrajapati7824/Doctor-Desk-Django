# Generated by Django 4.2 on 2023-05-31 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0015_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_registration',
            name='Patient_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
