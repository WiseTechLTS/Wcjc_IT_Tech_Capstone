# Generated by Django 5.1.5 on 2025-02-05 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospitalticket',
            old_name='patient_name',
            new_name='employee_name',
        ),
    ]
