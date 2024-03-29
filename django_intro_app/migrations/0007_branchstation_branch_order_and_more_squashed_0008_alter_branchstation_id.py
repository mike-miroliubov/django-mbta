# Generated by Django 5.0 on 2024-01-10 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('django_intro_app', '0007_branchstation_branch_order_and_more'), ('django_intro_app', '0008_alter_branchstation_id')]

    dependencies = [
        ('django_intro_app', '0006_alter_branchstation_options_alter_branch_stations_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='branchstation',
            index=models.Index(models.F('branch'), models.OrderBy(models.F('order')), name='branch_order'),
        ),
        migrations.AddConstraint(
            model_name='branchstation',
            constraint=models.UniqueConstraint(fields=('branch', 'station'), name='uq_branchstation_branch_station'),
        ),
        # migrations.AlterField(
        #     model_name='branchstation',
        #     name='id',
        #     field=models.UUIDField(primary_key=True, serialize=False),
        # ),
    ]
