from django.contrib import admin
from .models import Purchase

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['name','ps','quantity_buy','quantity_loss','package','price_unit', 'price_loss', 'price_checkout','part_id']

admin.site.register(Purchase, PurchaseAdmin)

