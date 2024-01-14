from django.db import migrations, models
import uuid

green_line = None
red_line = None
blue_line = None
orange_line = None
silver_line = None
green_b = None
green_c = None
green_d = None
green_e = None


class Migration(migrations.Migration):
    dependencies = [
        ('django_intro_app', '0009_branchstation_new_id_squashed_0012_rename_new_id_branchstation_id')
    ]

    def seed_lines(apps, schema_editor):
        Line = apps.get_model('django_intro_app', 'Line')
        global green_line, red_line, blue_line, orange_line, silver_line

        green_line = Line.objects.create(id=uuid.uuid4(), name='Green Line', color='green')
        red_line = Line.objects.create(id=uuid.uuid4(), name='Red Line', color='red')
        orange_line = Line.objects.create(id=uuid.uuid4(), name='Orange Line', color='orange')
        blue_line = Line.objects.create(id=uuid.uuid4(), name='Blue Line', color='blue')
        silver_line = Line.objects.create(id=uuid.uuid4(), name='Silver Line', color='silver')

    def seed_lines_reverse(apps, schema_editor):
        global green_line, red_line, blue_line, orange_line, silver_line
        # migrations are unapplied in the reverse order, so the lines have been already set by
        # seed_branches_reverse function
        green_line.delete()
        red_line.delete()
        orange_line.delete()
        blue_line.delete()
        silver_line.delete()

    def seed_branches(apps, schema_editor):
        Branch = apps.get_model('django_intro_app', 'Branch')

        global green_b, green_c, green_d, green_e

        green_b = Branch.objects.create(id=uuid.uuid4(), name='B', line=green_line, direction=0)
        green_c = Branch.objects.create(id=uuid.uuid4(), name='C', line=green_line, direction=0)
        green_d = Branch.objects.create(id=uuid.uuid4(), name='D', line=green_line, direction=0)
        green_e = Branch.objects.create(id=uuid.uuid4(), name='E', line=green_line, direction=0)

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
        global green_line, red_line, blue_line, orange_line, silver_line
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
        global green_b, green_c, green_d, green_e
        global green_line

        Station = apps.get_model('django_intro_app', 'Station')

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

        create_stations(green_c_stations, green_c, green_line)
        create_stations(green_b_stations, green_b, green_line)
        create_stations(green_d_stations, green_d, green_line)
        create_stations(green_e_stations, green_e, green_line)

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
