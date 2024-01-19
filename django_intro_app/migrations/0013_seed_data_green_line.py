from django.db import migrations, models
import uuid

green_line_uuid = uuid.UUID('f88c33b8-02bf-4abb-8b35-f4d063d39a2d')
red_line_uuid = uuid.UUID('3d33d693-59da-42e3-a010-8bc228239a10')
orange_line_uuid = uuid.UUID('cbf157c8-22b0-49cd-8f75-ce62935b7283')
blue_line_uuid = uuid.UUID('af55a708-cf8e-4a72-9d2c-af1f3a1aed32')
silver_line_uuid = uuid.UUID('58369f1a-6f68-4341-8a69-9de55ecfeb1e')
green_b_uuid = uuid.UUID('e06e79c1-d657-4837-ad37-35350136dfa3')
green_c_uuid = uuid.UUID('2fed3c3e-6d50-49f7-b406-70b441c3898c')
green_d_uuid = uuid.UUID('3f1c5f95-7ec4-4bbe-97ae-c3ceef3e3d47')
green_e_uuid = uuid.UUID('5a690d41-0b5c-478e-9075-06556ed93d63')

class Migration(migrations.Migration):
    dependencies = [
        ('django_intro_app', '0009_branchstation_new_id_squashed_0012_rename_new_id_branchstation_id')
    ]

    def seed_lines(apps, schema_editor):
        Line = apps.get_model('django_intro_app', 'Line')
        global green_line_uuid, silver_line_uuid, blue_line_uuid, orange_line_uuid, red_line_uuid

        Line.objects.create(id=green_line_uuid, name='Green Line', color='green')
        Line.objects.create(id=red_line_uuid, name='Red Line', color='red')
        Line.objects.create(id=orange_line_uuid, name='Orange Line', color='orange')
        Line.objects.create(id=blue_line_uuid, name='Blue Line', color='blue')
        Line.objects.create(id=silver_line_uuid, name='Silver Line', color='silver')

    def seed_lines_reverse(apps, schema_editor):
        global green_line_uuid, silver_line_uuid, blue_line_uuid, orange_line_uuid, red_line_uuid
        Line = apps.get_model('django_intro_app', 'Line')
        for line_uuid in [green_line_uuid, silver_line_uuid, blue_line_uuid, orange_line_uuid, red_line_uuid]:
            Line.objects.get(id=line_uuid).delete()

    def seed_branches(apps, schema_editor):
        Branch = apps.get_model('django_intro_app', 'Branch')
        Line = apps.get_model('django_intro_app', 'Line')

        global green_line_uuid
        global green_b_uuid, green_c_uuid, green_d_uuid, green_e_uuid

        green_line = Line.objects.get(id=green_line_uuid)
        red_line = Line.objects.get(id=red_line_uuid)
        blue_line = Line.objects.get(id=blue_line_uuid)
        orange_line = Line.objects.get(id=orange_line_uuid)
        silver_line = Line.objects.get(id=silver_line_uuid)
        Branch.objects.create(id=green_b_uuid, name='B', line=green_line, direction=0)
        Branch.objects.create(id=green_c_uuid, name='C', line=green_line, direction=0)
        Branch.objects.create(id=green_d_uuid, name='D', line=green_line, direction=0)
        Branch.objects.create(id=green_e_uuid, name='E', line=green_line, direction=0)

        Branch.objects.create(id=uuid.uuid4(), name='Ashmont', line=red_line, direction=0)
        Branch.objects.create(id=uuid.uuid4(), name='Mattapan', line=red_line, direction=0)
        Branch.objects.create(id=uuid.uuid4(), name='Braintree', line=red_line, direction=0)

        Branch.objects.create(id=uuid.uuid4(), name='Main', line=blue_line, direction=0)
        Branch.objects.create(id=uuid.uuid4(), name='Main', line=orange_line, direction=0)

        Branch.objects.create(id=uuid.uuid4(), name='SL1', line=silver_line, direction=0)
        Branch.objects.create(id=uuid.uuid4(), name='SL2', line=silver_line, direction=0)
        Branch.objects.create(id=uuid.uuid4(), name='SL3', line=silver_line, direction=0)
        Branch.objects.create(id=uuid.uuid4(), name='SL4', line=silver_line, direction=0)
        Branch.objects.create(id=uuid.uuid4(), name='SL5', line=silver_line, direction=0)

    def seed_branches_reverse(apps, schema_editor):
        Branch = apps.get_model('django_intro_app', 'Branch')
        Line = apps.get_model('django_intro_app', 'Line')

        green_line = Line.objects.get(color='green')
        red_line = Line.objects.get(color='red')
        orange_line = Line.objects.get(color='orange')
        blue_line = Line.objects.get(color='blue')
        silver_line = Line.objects.get(color='silver')

        Branch.objects.filter(line=green_line).delete()
        Branch.objects.filter(line=blue_line).delete()
        Branch.objects.filter(line=red_line).delete()
        Branch.objects.filter(line=orange_line).delete()
        Branch.objects.filter(line=silver_line).delete()

    def seed_stations(apps, schema_editor):
        global green_b_uuid, green_c_uuid, green_d_uuid, green_e_uuid
        global green_line_uuid
        Line = apps.get_model('django_intro_app', 'Line')
        green_line = Line.objects.get(id=green_line_uuid)

        Station = apps.get_model('django_intro_app', 'Station')
        Branch = apps.get_model('django_intro_app', 'Branch')

        stations_cache = {}

        def create_stations(branch_stations, branch, line):
            for i, station_name in enumerate(branch_stations):
                station = stations_cache.get(station_name)
                if not station:
                    station = Station.objects.create(id=uuid.uuid4(), name=station_name, line=line)
                    stations_cache[station_name] = station

                branch.stations.add(station, through_defaults={'order': i + 1, 'id': uuid.uuid4()})

        green_c_stations = ["Government Center", "Park Street", "Boylston", "Arlington", "Copley",
                            "Hynes Convention Center", "Kenmore", "Saint Mary's Street", "Hawes Street", "Kent Street",
                            "Saint Paul Street", "Coolidge Corner", "Summit Avenue", "Brandon Hall", "Fairbanks Street",
                            "Washington Square", "Tappan Street", "Dean Road", "Englewood Avenue", "Cleveland Circle"]
        green_b_stations = ["Government Center", "Park Street", "Boylston", "Arlington", "Copley",
                            "Hynes Convention Center", "Kenmore", "Blandford Street", "Boston University East",
                            "Boston University Central", "Amory Street", "Babcock Street", "Packard's Corner",
                            "Harvard Avenue", "Griggs Street", "Allston Street", "Warren Street", "Washington Street",
                            "Sutherland Road", "Chiswick Road", "Chestnut Hill Avenue", "South Street",
                            "Boston College"]
        green_d_stations = ["Union Square", "Lechmere", "Science Park/West End", "North Station", "Haymarket",
                            "Government Center", "Park Street", "Boylston", "Arlington", "Copley",
                            "Hynes Convention Center", "Kenmore", "Fenway", "Longwood", "Brookline Village",
                            "Brookline Hills", "Beaconsfield", "Reservoir", "Chestnut Hill", "Newton Centre",
                            "Newton Highlands", "Eliot", "Waban", "Woodland", "Riverside"]
        green_e_stations = ["Medford/Tufts", "Ball Square", "Magoun Square", "Gilman Square",
                            "East Somerville", "Lechmere", "Science Park/West End", "North Station", "Haymarket",
                            "Government Center", "Park Street", "Arlington", "Copley", "Prudential", "Symphony",
                            "Northeastern University", "Museum of Fine Arts", "Longwood Medical Area",
                            "Brigham Circle", "Fenwood Road", "Mission Park", "Riverway", "Back of the Hill",
                            "Heath Street"]

        create_stations(green_c_stations, Branch.objects.get(id=green_c_uuid), green_line)
        create_stations(green_b_stations, Branch.objects.get(id=green_b_uuid), green_line)
        create_stations(green_d_stations, Branch.objects.get(id=green_d_uuid), green_line)
        create_stations(green_e_stations, Branch.objects.get(id=green_e_uuid), green_line)

    def seed_stations_reverse(apps, schema_editor):
        Station = apps.get_model('django_intro_app', 'Station')
        BranchStation = apps.get_model('django_intro_app', 'BranchStation')
        BranchStation.objects.all().delete()
        Station.objects.all().delete()

    operations = [
        migrations.AlterField(
            model_name='branchstation',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False, default=uuid.uuid4()),
        ),
        migrations.RunPython(seed_lines, reverse_code=seed_lines_reverse),
        migrations.RunPython(seed_branches, reverse_code=seed_branches_reverse),
        migrations.RunPython(seed_stations, reverse_code=seed_stations_reverse)
    ]
