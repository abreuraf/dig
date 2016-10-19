# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Cachedimage(models.Model):
    originalid = models.IntegerField(db_column='originalId')  # Field name made lowercase.
    originaltype = models.CharField(db_column='originalType', max_length=255)  # Field name made lowercase.
    cachefile = models.CharField(db_column='cacheFile', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'CachedImage'


class Cronlogger(models.Model):
    lastrundate = models.DateTimeField(db_column='lastRunDate')  # Field name made lowercase.
    cronjob = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'CronLogger'


class Distributor(models.Model):
    name = models.CharField(unique=True, max_length=255)
    address = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    skuurl = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Distributor'


class Fosuser(models.Model):
    username = models.CharField(max_length=255)
    username_canonical = models.CharField(unique=True, max_length=255)
    enabled = models.IntegerField()
    salt = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(blank=True, null=True)
    locked = models.IntegerField()
    expired = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)
    confirmation_token = models.CharField(max_length=255, blank=True, null=True)
    password_requested_at = models.DateTimeField(blank=True, null=True)
    roles = models.TextField()
    credentials_expired = models.IntegerField()
    credentials_expire_at = models.DateTimeField(blank=True, null=True)
    email_canonical = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'FOSUser'


class Footprint(models.Model):
    category = models.ForeignKey('Footprintcategory', blank=True, null=True)
    name = models.CharField(unique=True, max_length=64)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Footprint'


class Footprintattachment(models.Model):
    footprint = models.ForeignKey(Footprint, blank=True, null=True)
    type = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    originalname = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=255)
    size = models.IntegerField()
    extension = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'FootprintAttachment'


class Footprintcategory(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    lft = models.IntegerField()
    rgt = models.IntegerField()
    lvl = models.IntegerField()
    root = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    categorypath = models.TextField(db_column='categoryPath', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'FootprintCategory'


class Footprintimage(models.Model):
    footprint = models.ForeignKey(Footprint, unique=True, blank=True, null=True)
    type = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    originalname = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=255)
    size = models.IntegerField()
    extension = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'FootprintImage'


class Manufacturer(models.Model):
    name = models.CharField(unique=True, max_length=255)
    address = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Manufacturer'


class Manufacturericlogo(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True)
    type = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    originalname = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=255)
    size = models.IntegerField()
    extension = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'ManufacturerICLogo'


class Part(models.Model):
    category = models.ForeignKey('Partcategory', blank=True, null=True)
    footprint = models.ForeignKey(Footprint, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField()
    stocklevel = models.IntegerField(db_column='stockLevel')  # Field name made lowercase.
    minstocklevel = models.IntegerField(db_column='minStockLevel')  # Field name made lowercase.
    averageprice = models.DecimalField(db_column='averagePrice', max_digits=13, decimal_places=4,null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True)
    needsreview = models.IntegerField(db_column='needsReview')  # Field name made lowercase.
    partcondition = models.CharField(db_column='partCondition', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)  # Field name made lowercase.
    internalpartnumber = models.CharField(db_column='internalPartNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    removals = models.IntegerField(null=True)
    lowstock = models.IntegerField(db_column='lowStock')  # Field name made lowercase.
    partunit = models.ForeignKey('Partunit', db_column='partUnit_id', blank=True, null=True)  # Field name made lowercase.
    storagelocation = models.ForeignKey('Storagelocation', db_column='storageLocation_id', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Part'


class Partattachment(models.Model):
    part = models.ForeignKey(Part, blank=True, null=True)
    type = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    originalname = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=255)
    size = models.IntegerField()
    extension = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    isimage = models.IntegerField(db_column='isImage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PartAttachment'


class Partcategory(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    lft = models.IntegerField()
    rgt = models.IntegerField()
    lvl = models.IntegerField()
    root = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    categorypath = models.TextField(db_column='categoryPath', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PartCategory'


class Partdistributor(models.Model):
    part = models.ForeignKey(Part, blank=True, null=True)
    distributor = models.ForeignKey(Distributor, blank=True, null=True)
    ordernumber = models.CharField(db_column='orderNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    packagingunit = models.IntegerField(db_column='packagingUnit')  # Field name made lowercase.
    price = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'PartDistributor'


class Partimage(models.Model):
    part = models.ForeignKey(Part, blank=True, null=True)
    type = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    originalname = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=255)
    size = models.IntegerField()
    extension = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'PartImage'


class Partkeepruser(models.Model):
    provider = models.ForeignKey('Userprovider', blank=True, null=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    admin = models.IntegerField()
    legacy = models.IntegerField()
    lastseen = models.DateTimeField(db_column='lastSeen', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField()
    protected = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'PartKeeprUser'
        unique_together = (('username', 'provider_id'),)


class Partmanufacturer(models.Model):
    part = models.ForeignKey(Part, blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True)
    partnumber = models.CharField(db_column='partNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PartManufacturer'


class Partparameter(models.Model):
    part = models.ForeignKey(Part, blank=True, null=True)
    unit = models.ForeignKey('Unit', blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    value = models.FloatField()
    rawvalue = models.FloatField(db_column='rawValue')  # Field name made lowercase.
    siprefix = models.ForeignKey('Siprefix', db_column='siPrefix_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'PartParameter'


class Partunit(models.Model):
    name = models.CharField(max_length=255)
    shortname = models.CharField(db_column='shortName', max_length=255)  # Field name made lowercase.
    is_default = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'PartUnit'


class Project(models.Model):
    user = models.ForeignKey(Partkeepruser, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Project'


class Projectattachment(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True)
    type = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    originalname = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=255)
    size = models.IntegerField()
    extension = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'ProjectAttachment'


class Projectpart(models.Model):
    part = models.ForeignKey(Part, blank=True, null=True)
    project = models.ForeignKey(Project, blank=True, null=True)
    quantity = models.IntegerField()
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ProjectPart'


class Schemaversions(models.Model):
    version = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'SchemaVersions'


class Siprefix(models.Model):
    prefix = models.CharField(max_length=255)
    symbol = models.CharField(max_length=2)
    exponent = models.IntegerField()
    base = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'SiPrefix'


class Statisticsnapshot(models.Model):
    datetime = models.DateTimeField(db_column='dateTime')  # Field name made lowercase.
    parts = models.IntegerField()
    categories = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'StatisticSnapshot'


class Statisticsnapshotunit(models.Model):
    stocklevel = models.IntegerField(db_column='stockLevel')  # Field name made lowercase.
    statisticsnapshot = models.ForeignKey(Statisticsnapshot, db_column='statisticSnapshot_id', blank=True, null=True)  # Field name made lowercase.
    partunit = models.ForeignKey(Partunit, db_column='partUnit_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'StatisticSnapshotUnit'


class Stockentry(models.Model):
    part = models.ForeignKey(Part, blank=True, null=True)
    user = models.ForeignKey(Partkeepruser, blank=True, null=True)
    stocklevel = models.IntegerField(db_column='stockLevel')  # Field name made lowercase.
    price = models.DecimalField(max_digits=13, decimal_places=4, blank=True, null=True)
    datetime = models.DateTimeField(db_column='dateTime')  # Field name made lowercase.
    correction = models.IntegerField()
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'StockEntry'


class Storagelocation(models.Model):
    category = models.ForeignKey('Storagelocationcategory', blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'StorageLocation'


class Storagelocationcategory(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    lft = models.IntegerField()
    rgt = models.IntegerField()
    lvl = models.IntegerField()
    root = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    categorypath = models.TextField(db_column='categoryPath', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'StorageLocationCategory'


class Storagelocationimage(models.Model):
    type = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    originalname = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=255)
    size = models.IntegerField()
    extension = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    storagelocation = models.ForeignKey(Storagelocation, db_column='storageLocation_id', unique=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'StorageLocationImage'


class Systemnotice(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    acknowledged = models.IntegerField()
    type = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'SystemNotice'


class Systempreference(models.Model):
    preferencekey = models.CharField(db_column='preferenceKey', primary_key=True, max_length=255)  # Field name made lowercase.
    preferencevalue = models.TextField(db_column='preferenceValue')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SystemPreference'


class Tempimage(models.Model):
    type = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    originalname = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=255)
    size = models.IntegerField()
    extension = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'TempImage'


class Tempuploadedfile(models.Model):
    type = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    originalname = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=255)
    size = models.IntegerField()
    extension = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'TempUploadedFile'


class Tipoftheday(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'TipOfTheDay'


class Tipofthedayhistory(models.Model):
    user = models.ForeignKey(Partkeepruser, blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'TipOfTheDayHistory'


class Unit(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'Unit'


class Unitsiprefixes(models.Model):
    unit = models.ForeignKey(Unit)
    siprefix = models.ForeignKey(Siprefix)

    class Meta:
        managed = True
        db_table = 'UnitSiPrefixes'
        unique_together = (('unit_id', 'siprefix_id'),)


class Userpreference(models.Model):
    user = models.ForeignKey(Partkeepruser)
    preferencekey = models.CharField(db_column='preferenceKey', max_length=255)  # Field name made lowercase.
    preferencevalue = models.TextField(db_column='preferenceValue')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'UserPreference'
        unique_together = (('preferenceKey', 'user_id'),)


class Userprovider(models.Model):
    type = models.CharField(unique=True, max_length=255)
    editable = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'UserProvider'
