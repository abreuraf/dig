from django.db import models
from django.forms import ModelForm
from digstock.models import Part
from purchases.models import Purchase

class Production(models.Model):
    bom_name = models.CharField(max_length=255)
    bom_file = models.FileField(upload_to='bom', default=True)
    bom_version = models.CharField(max_length=255)
    name_enterprise = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    date_production = models.DateTimeField()
    date_return = models.DateTimeField()
    def __str__(self):
        return self.bom_name
    def get_bom_itens(self):
        list = Part.objects.all()
        return  len(list)

