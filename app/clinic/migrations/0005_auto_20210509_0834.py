# Generated by Django 3.0 on 2021-05-09 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0004_auto_20210508_2021'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MedicalUser',
            new_name='StaffProfile',
        ),
    ]
