from django.contrib import admin

from .models import Production

class ProductionAdmin(admin.ModelAdmin):
    list_display = ['bom_name', 'bom_file','bom_version','name_enterprise','contact','info','date_production','date_return']

admin.site.register(Production, ProductionAdmin)
   
