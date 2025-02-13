# Generated by Django 5.1.5 on 2025-02-06 02:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('closed', 'Closed')], default='open', help_text='Current status of the ticket.', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ParentDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, help_text='Optional description of the department.', null=True)),
            ],
            options={
                'verbose_name': 'Parent Department',
                'verbose_name_plural': 'Parent Departments',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SubDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('priority', models.PositiveIntegerField(help_text='Lower numbers indicate higher operational priority within the parent department.')),
                ('parent_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_departments', to='ticket_api.parentdepartment')),
            ],
            options={
                'verbose_name': 'Sub Department',
                'verbose_name_plural': 'Sub Departments',
                'ordering': ['parent_department', 'priority'],
                'unique_together': {('name', 'parent_department')},
            },
        ),
        migrations.CreateModel(
            name='HospitalTicket',
            fields=[
                ('ticket', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='hospital_ticket', serialize=False, to='ticket_api.ticket')),
                ('patient_id', models.CharField(blank=True, help_text='Identifier for the patient involved (if applicable).', max_length=50, null=True)),
                ('room_number', models.CharField(blank=True, help_text='Room number associated with the ticket (if applicable).', max_length=20, null=True)),
                ('additional_info', models.TextField(blank=True, help_text='Any additional hospital-specific information.', null=True)),
            ],
            options={
                'verbose_name': 'Hospital Ticket',
                'verbose_name_plural': 'Hospital Tickets',
            },
        ),
        migrations.AddField(
            model_name='ticket',
            name='sub_department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='ticket_api.subdepartment'),
        ),
    ]
