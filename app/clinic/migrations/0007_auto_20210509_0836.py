# Generated by Django 3.0 on 2021-05-09 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0006_auto_20210509_0836'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClinicStaffProfile',
            new_name='StaffProfile',
        ),
    ]
