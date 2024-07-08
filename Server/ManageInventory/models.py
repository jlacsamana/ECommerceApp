from django.db import models


# Create your models here.
class InventoryItem(models.Model):
    """standard inventory item"""

    upc = models.CharField(max_length=26)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    is_second_hand = models.BooleanField(default=False)

    # optional fields
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    product_series = models.CharField(max_length=100, blank=True, null=True)

    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = (("upc", "is_second_hand"),)
