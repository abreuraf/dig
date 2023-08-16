# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cachedimage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('originalid', models.IntegerField(db_column='originalId')),
                ('originaltype', models.CharField(db_column='originalType', max_length=255)),
                ('cachefile', models.CharField(db_column='cacheFile', max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'CachedImage',
            },
        ),
        migrations.CreateModel(
            name='Cronlogger',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lastrundate', models.DateTimeField(db_column='lastRunDate')),
                ('cronjob', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'managed': False,
                'db_table': 'CronLogger',
            },
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('url', models.CharField(max_length=255, null=True, blank=True)),
                ('phone', models.CharField(max_length=255, null=True, blank=True)),
                ('fax', models.CharField(max_length=255, null=True, blank=True)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('skuurl', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Distributor',
            },
        ),
        migrations.CreateModel(
            name='Footprint',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Footprint',
            },
        ),
        migrations.CreateModel(
            name='Footprintattachment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=255)),
                ('filename', models.CharField(max_length=255)),
                ('originalname', models.CharField(max_length=255, null=True, blank=True)),
                ('mimetype', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('extension', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'FootprintAttachment',
            },
        ),
        migrations.CreateModel(
            name='Footprintcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lft', models.IntegerField()),
                ('rgt', models.IntegerField()),
                ('lvl', models.IntegerField()),
                ('root', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(null=True, blank=True)),
                ('categorypath', models.TextField(db_column='categoryPath', null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'FootprintCategory',
            },
        ),
        migrations.CreateModel(
            name='Footprintimage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=255)),
                ('filename', models.CharField(max_length=255)),
                ('originalname', models.CharField(max_length=255, null=True, blank=True)),
                ('mimetype', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('extension', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'FootprintImage',
            },
        ),
        migrations.CreateModel(
            name='Fosuser',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=255)),
                ('username_canonical', models.CharField(max_length=255, unique=True)),
                ('enabled', models.IntegerField()),
                ('salt', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('locked', models.IntegerField()),
                ('expired', models.IntegerField()),
                ('expires_at', models.DateTimeField(null=True, blank=True)),
                ('confirmation_token', models.CharField(max_length=255, null=True, blank=True)),
                ('password_requested_at', models.DateTimeField(null=True, blank=True)),
                ('roles', models.TextField()),
                ('credentials_expired', models.IntegerField()),
                ('credentials_expire_at', models.DateTimeField(null=True, blank=True)),
                ('email_canonical', models.CharField(max_length=255, null=True, blank=True)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'FOSUser',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('url', models.CharField(max_length=255, null=True, blank=True)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('phone', models.CharField(max_length=255, null=True, blank=True)),
                ('fax', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Manufacturer',
            },
        ),
        migrations.CreateModel(
            name='Manufacturericlogo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=255)),
                ('filename', models.CharField(max_length=255)),
                ('originalname', models.CharField(max_length=255, null=True, blank=True)),
                ('mimetype', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('extension', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'ManufacturerICLogo',
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('comment', models.TextField()),
                ('stocklevel', models.IntegerField(db_column='stockLevel')),
                ('minstocklevel', models.IntegerField(db_column='minStockLevel')),
                ('averageprice', models.DecimalField(db_column='averagePrice', max_digits=13, decimal_places=4)),
                ('status', models.CharField(max_length=255, null=True, blank=True)),
                ('needsreview', models.IntegerField(db_column='needsReview')),
                ('partcondition', models.CharField(db_column='partCondition', null=True, max_length=255, blank=True)),
                ('createdate', models.DateTimeField(db_column='createDate', null=True, blank=True)),
                ('internalpartnumber', models.CharField(db_column='internalPartNumber', null=True, max_length=255, blank=True)),
                ('removals', models.IntegerField()),
                ('lowstock', models.IntegerField(db_column='lowStock')),
            ],
            options={
                'managed': False,
                'db_table': 'Part',
            },
        ),
        migrations.CreateModel(
            name='Partattachment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=255)),
                ('filename', models.CharField(max_length=255)),
                ('originalname', models.CharField(max_length=255, null=True, blank=True)),
                ('mimetype', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('extension', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField()),
                ('isimage', models.IntegerField(db_column='isImage', null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'PartAttachment',
            },
        ),
        migrations.CreateModel(
            name='Partcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lft', models.IntegerField()),
                ('rgt', models.IntegerField()),
                ('lvl', models.IntegerField()),
                ('root', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(null=True, blank=True)),
                ('categorypath', models.TextField(db_column='categoryPath', null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'PartCategory',
            },
        ),
        migrations.CreateModel(
            name='Partdistributor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ordernumber', models.CharField(db_column='orderNumber', null=True, max_length=255, blank=True)),
                ('packagingunit', models.IntegerField(db_column='packagingUnit')),
                ('price', models.DecimalField(max_digits=13, decimal_places=4, null=True, blank=True)),
                ('sku', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'PartDistributor',
            },
        ),
        migrations.CreateModel(
            name='Partimage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=255)),
                ('filename', models.CharField(max_length=255)),
                ('originalname', models.CharField(max_length=255, null=True, blank=True)),
                ('mimetype', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('extension', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'PartImage',
            },
        ),
        migrations.CreateModel(
            name='Partkeepruser',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=32, null=True, blank=True)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
                ('admin', models.IntegerField()),
                ('legacy', models.IntegerField()),
                ('lastseen', models.DateTimeField(db_column='lastSeen', null=True, blank=True)),
                ('active', models.IntegerField()),
                ('protected', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'PartKeeprUser',
            },
        ),
        migrations.CreateModel(
            name='Partmanufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('partnumber', models.CharField(db_column='partNumber', null=True, max_length=255, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'PartManufacturer',
            },
        ),
        migrations.CreateModel(
            name='Partparameter',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('value', models.FloatField()),
                ('rawvalue', models.FloatField(db_column='rawValue')),
            ],
            options={
                'managed': False,
                'db_table': 'PartParameter',
            },
        ),
        migrations.CreateModel(
            name='Partunit',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('shortname', models.CharField(db_column='shortName', max_length=255)),
                ('is_default', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'PartUnit',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Project',
            },
        ),
        migrations.CreateModel(
            name='Projectattachment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=255)),
                ('filename', models.CharField(max_length=255)),
                ('originalname', models.CharField(max_length=255, null=True, blank=True)),
                ('mimetype', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('extension', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'ProjectAttachment',
            },
        ),
        migrations.CreateModel(
            name='Projectpart',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('remarks', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'ProjectPart',
            },
        ),
        migrations.CreateModel(
            name='Schemaversions',
            fields=[
                ('version', models.CharField(max_length=255, serialize=False, primary_key=True)),
            ],
            options={
                'managed': False,
                'db_table': 'SchemaVersions',
            },
        ),
        migrations.CreateModel(
            name='Siprefix',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('prefix', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=2)),
                ('exponent', models.IntegerField()),
                ('base', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'SiPrefix',
            },
        ),
        migrations.CreateModel(
            name='Statisticsnapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('datetime', models.DateTimeField(db_column='dateTime')),
                ('parts', models.IntegerField()),
                ('categories', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'StatisticSnapshot',
            },
        ),
        migrations.CreateModel(
            name='Statisticsnapshotunit',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('stocklevel', models.IntegerField(db_column='stockLevel')),
            ],
            options={
                'managed': False,
                'db_table': 'StatisticSnapshotUnit',
            },
        ),
        migrations.CreateModel(
            name='Stockentry',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('stocklevel', models.IntegerField(db_column='stockLevel')),
                ('price', models.DecimalField(max_digits=13, decimal_places=4, null=True, blank=True)),
                ('datetime', models.DateTimeField(db_column='dateTime')),
                ('correction', models.IntegerField()),
                ('comment', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'StockEntry',
            },
        ),
        migrations.CreateModel(
            name='Storagelocation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'managed': False,
                'db_table': 'StorageLocation',
            },
        ),
        migrations.CreateModel(
            name='Storagelocationcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lft', models.IntegerField()),
                ('rgt', models.IntegerField()),
                ('lvl', models.IntegerField()),
                ('root', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(null=True, blank=True)),
                ('categorypath', models.TextField(db_column='categoryPath', null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'StorageLocationCategory',
            },
        ),
        migrations.CreateModel(
            name='Storagelocationimage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=255)),
                ('filename', models.CharField(max_length=255)),
                ('originalname', models.CharField(max_length=255, null=True, blank=True)),
                ('mimetype', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('extension', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'StorageLocationImage',
            },
        ),
        migrations.CreateModel(
            name='Systemnotice',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('acknowledged', models.IntegerField()),
                ('type', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'SystemNotice',
            },
        ),
        migrations.CreateModel(
            name='Systempreference',
            fields=[
                ('preferencekey', models.CharField(db_column='preferenceKey', serialize=False, max_length=255, primary_key=True)),
                ('preferencevalue', models.TextField(db_column='preferenceValue')),
            ],
            options={
                'managed': False,
                'db_table': 'SystemPreference',
            },
        ),
        migrations.CreateModel(
            name='Tempimage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=255)),
                ('filename', models.CharField(max_length=255)),
                ('originalname', models.CharField(max_length=255, null=True, blank=True)),
                ('mimetype', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('extension', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'TempImage',
            },
        ),
        migrations.CreateModel(
            name='Tempuploadedfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=255)),
                ('filename', models.CharField(max_length=255)),
                ('originalname', models.CharField(max_length=255, null=True, blank=True)),
                ('mimetype', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('extension', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'TempUploadedFile',
            },
        ),
        migrations.CreateModel(
            name='Tipoftheday',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'TipOfTheDay',
            },
        ),
        migrations.CreateModel(
            name='Tipofthedayhistory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'TipOfTheDayHistory',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'Unit',
            },
        ),
        migrations.CreateModel(
            name='Unitsiprefixes',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
            ],
            options={
                'managed': False,
                'db_table': 'UnitSiPrefixes',
            },
        ),
        migrations.CreateModel(
            name='Userpreference',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('preferencekey', models.CharField(db_column='preferenceKey', max_length=255)),
                ('preferencevalue', models.TextField(db_column='preferenceValue')),
            ],
            options={
                'managed': False,
                'db_table': 'UserPreference',
            },
        ),
        migrations.CreateModel(
            name='Userprovider',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=255, unique=True)),
                ('editable', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'UserProvider',
            },
        ),
    ]
