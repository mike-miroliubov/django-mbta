# Generated by Django 5.0 on 2024-01-14 21:24

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('django_intro_app', '0014_remove_train_line_train_branch_and_more'), ('django_intro_app', '0015_alter_branchstation_id_alter_train_branch')]

    dependencies = [
        ('django_intro_app', '0013_seed_data_green_line'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train',
            name='line',
        ),
        migrations.AlterField(
            model_name='branchstation',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='train',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='django_intro_app.branch'),
        ),
    ]
