from django.contrib import admin
from .models import Part

class PartAdmin(admin.ModelAdmin):
    fields_display = ['name'] 

admin.site.register(Part)

