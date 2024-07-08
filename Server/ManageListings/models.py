from django.db import models
from ManageInventory.models import InventoryItem


# Create your models here.
class Listing(models.Model):
    """a (cross)post for an item"""

    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    price = models.FloatField()

    # is posting listed on these platforms?
    onWooCommerce = models.BooleanField(default=False)
    onEbay = models.BooleanField(default=False)
    onAmazon = models.BooleanField(default=False)
    onFBMarketplace = models.BooleanField(default=False)
