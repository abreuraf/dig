from django.contrib import admin

from .models import Purchase

class PurchaseAdmin(admin.ModelAdmin):
    #fields = ['part_id','ps','qtd_purchase','price_last'] // select fields show only
    list_display = ['part_id','quantity_buy']

admin.site.register(Purchase, PurchaseAdmin)

