from django.db import migrations, models
import uuid

def populate_unique_ids(apps, schema_editor):
    Ticket = apps.get_model('tickets', 'Ticket')
    for ticket in Ticket.objects.all():
        ticket.unique_id = uuid.uuid4()  # Assign a unique UUID
        ticket.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),  # Adjust to your actual initial migration file
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='unique_id',
            field=models.UUIDField(default=None, editable=False, unique=True, null=True),
        ),
        migrations.RunPython(populate_unique_ids),
        migrations.AlterField(
            model_name='ticket',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
