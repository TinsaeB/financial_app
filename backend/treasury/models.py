from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    initial_value = models.DecimalField(max_digits=10, decimal_places=2)
    current_value = models.DecimalField(max_digits=10, decimal_places=2)
    depreciation_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
