# Generated by Django 4.2 on 2023-04-29 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorRegistrationdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctor_Name', models.CharField(default='', max_length=1000)),
                ('Phone_Number', models.EmailField(max_length=254)),
                ('Email_id', models.CharField(default='', max_length=10)),
                ('City', models.IntegerField(default=0)),
                ('Clinic_Name', models.CharField(default='', max_length=10)),
                ('Password', models.CharField(default='', max_length=10)),
                ('Confirm_Password', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
