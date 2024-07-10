from django.db import models
from ManageInventory.models import InventoryItem


# Create your models here.
class Listing(models.Model):
    """a (cross)post for an item"""

    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    price = models.FloatField()
    additional_description = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
    )

    # is posting listed on these platforms?
    on_WooCommerce = models.BooleanField(default=False)
    on_Ebay = models.BooleanField(default=False)
    on_Amazon = models.BooleanField(default=False)
    on_FBMarketplace = models.BooleanField(default=False)
