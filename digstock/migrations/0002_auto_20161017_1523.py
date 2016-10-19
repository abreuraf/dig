# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digstock', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cachedimage',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='cronlogger',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='distributor',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='footprint',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='footprintattachment',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='footprintcategory',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='footprintimage',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='fosuser',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='manufacturericlogo',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='part',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='partattachment',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='partcategory',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='partdistributor',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='partimage',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='partkeepruser',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='partmanufacturer',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='partparameter',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='partunit',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='projectattachment',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='projectpart',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='schemaversions',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='siprefix',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='statisticsnapshot',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='statisticsnapshotunit',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='stockentry',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='storagelocation',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='storagelocationcategory',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='storagelocationimage',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='systemnotice',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='systempreference',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tempimage',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tempuploadedfile',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tipoftheday',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='tipofthedayhistory',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='unitsiprefixes',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='userpreference',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='userprovider',
            options={'managed': True},
        ),
    ]
