# Generated by Django 4.2.5 on 2023-10-04 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='BookingId',
        ),
    ]