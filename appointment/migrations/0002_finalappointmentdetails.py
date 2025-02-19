# Generated by Django 5.1.6 on 2025-02-19 23:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalAppointmentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctorname')),
                ('doctor_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctortype')),
                ('visit_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.appointmentdates')),
            ],
        ),
    ]
