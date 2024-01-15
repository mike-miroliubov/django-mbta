import uuid

from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('django_intro_app', '0016_trackingdevice_trainregistration'),
    ]

    def seed_trains(apps, schema_editor):
        Train = apps.get_model('django_intro_app', 'Train')
        Branch = apps.get_model('django_intro_app', 'Branch')
        train1 = Train.objects.create(id=uuid.uuid4(), name='TC123X1')

    operations = [
        migrations.RunPython(seed_trains, reverse_code=migrations.RunPython.noop)
    ]