from django.db import models

class Purchase(models.Model):
    part_id = models.CharField(max_length=255)
    ps = models.IntegerField()
    quantity_buy = models.IntegerField()
    quantity_loss = models.IntegerField()
    package = models.CharField(max_length=255)
    price_unit = models.DecimalField(max_digits=30,decimal_places=2)
    price_loss = models.DecimalField(max_digits=30,decimal_places=2)
    price_checkout = models.DecimalField(max_digits=30,decimal_places=2)
    def __str__(self):
        return self.part_id

