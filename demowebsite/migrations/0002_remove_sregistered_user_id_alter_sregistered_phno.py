# Generated by Django 4.0 on 2022-01-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demowebsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sregistered',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='sregistered',
            name='phno',
            field=models.CharField(max_length=10),
        ),
    ]