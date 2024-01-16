import uuid

from django.db import migrations, models

b_trains = ['VD7WNAQZ', 'J6AYY7FH', '6RS625Y4', 'N99TORB4', 'MQTMXNQS', 'P7GFQSHE', 'JXZEFOI3', '6UY1ONI9', 'EMRVA8F8',
            '6U7AIJOX']
c_trains = ['AQGKDC1H', 'UM3JNP6A', 'LD5DTUB3', '3CVBB2XP', '7TGJEOJC', '64228HI3', 'H6DRCM3S', 'W4QDM10K', 'ON09RKT1',
            'TWH4T3YW']
d_trains = ['EI2NGGBF', 'PWCSAE5Y', 'NFX10089', 'Y3YCUUN9', 'PE9SRDDM', 'MMYOIDAX', 'CMUF1QHW', 'E1EJ46GN']
e_trains = ['DDILMGLW', 'YE0LVJF7', 'B70TA842', 'OMVSKSMX', 'W0LCWI5E']


class Migration(migrations.Migration):
    dependencies = [
        ('django_intro_app', '0016_trackingdevice_trainregistration'),
    ]

    def seed_trains(apps, schema_editor):
        Train = apps.get_model('django_intro_app', 'Train')
        Branch = apps.get_model('django_intro_app', 'Branch')

        green_b = Branch.objects.get(name='B')
        green_c = Branch.objects.get(name='C')
        green_d = Branch.objects.get(name='D')
        green_e = Branch.objects.get(name='E')

        for branch, trains in [(green_b, b_trains), (green_c, c_trains), (green_d, d_trains), (green_e, e_trains)]:
            for train_name in trains:
                Train.objects.create(id=uuid.uuid4(), name=train_name, branch=branch)

    operations = [
        migrations.RunPython(seed_trains, reverse_code=migrations.RunPython.noop)
    ]
