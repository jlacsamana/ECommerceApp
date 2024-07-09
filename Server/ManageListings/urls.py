from django.urls import path
from .views import (
    test,
    get_listings,
    get_listing,
    post_new_listing,
    edit_listing,
    delete_listing,
)

urlpatterns = [
    path("test", test, name="test"),
    path("", get_listings, name="get-listing"),
    path("<int:id>", get_listing, name="get-listing-by-id"),
    path("", post_new_listing, name="post-listing"),
    path("", edit_listing, name="edit-listing"),
    path("<int:id>", delete_listing, name="delete-listing"),
]
