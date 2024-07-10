from django.urls import path
from .views import test, route_handler, route_handler_with_id

urlpatterns = [
    path("listings/test/", test, name="test"),
    path("listings/", route_handler, name="handler"),
    path("listings/<int:id>", route_handler_with_id, name="handler-with-id"),
]
