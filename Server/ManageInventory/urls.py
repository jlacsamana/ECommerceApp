from django.urls import path
from .views import (
    test,
    get_inventory_items,
    get_inventory_item,
    post_new_inventory_item,
    edit_inventory_item,
    delete_inventory_item,
)

urlpatterns = [
    path("test", test, name="test"),
    path("", get_inventory_items, name="get-items"),
    path("<str:id>", get_inventory_item, name="get-item-by-id"),
    path("", post_new_inventory_item, name="post-item"),
    path("", edit_inventory_item, name="edit-item"),
    path("<str:id>", delete_inventory_item, name="delete-item"),
]
