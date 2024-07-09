from django.urls import path
from .views import (
    test,
    route_handler,
    route_handler_with_id,
)

urlpatterns = [
    path("inventory/test/", test, name="test"),
    path("inventory/", route_handler, name="handler"),
    path("inventory/<int:id>", route_handler_with_id, name="handler-with-id"),
]
