# Generated by Django 4.0 on 2022-01-16 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demowebsite', '0013_rename_number_appointment_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]
