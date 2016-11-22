from django.db import models
from django.forms import ModelForm
from digstock.models import Part
from purchases.models import Purchase
import os, xlrd, sys



class Production(models.Model):
    bom_name = models.CharField(max_length=255)
    bom_file = models.FileField(upload_to='bom/')
    bom_version = models.CharField(max_length=255)
    name_enterprise = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    date_production = models.DateTimeField()
    date_return = models.DateTimeField()
    

    def __str__(self):
        return self.bom_name  

    def get_compare_itens(self):
        parts = self.get_part_itens()
        bom_itens = self.get_bom_itens()
        lf = []
        for i in bom_itens:            
            for j in parts:
                if i[0] == j[0]:
                    lf.append((i[0], i[1], j[1], (j[1] - i[1])))             
        return lf

    def get_part_itens(self):
        list_parts = []
        for n in Part.objects.all():
            list_parts.append((n.name, n.stocklevel))
        return list_parts

    def get_bom_itens(self):
        list_bom = []
        wb = xlrd.open_workbook(self.bom_file.file.name) 
        sh = wb.sheet_by_index(0) 
        
        for ry in range(sh.nrows):
            ncols = 0
            if sh.ncols == 20:
                col_q = 19
            else:
                col_q = 20
            list_bom.append((sh.cell_value(rowx=ry, colx=1),sh.cell_value(rowx=ry, colx=col_q))) 

        list_bom.pop(0)
        list_bom = sorted(list_bom)       

        return list_bom         

        
