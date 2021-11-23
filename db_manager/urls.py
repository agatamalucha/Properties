from django.urls import path, include
from db_manager.views import db_manager,property_upload

app_name = "db_manager"

urlpatterns = [
    path("", db_manager, name="db-manager"),
    path("property-upload", property_upload, name="property-upload"),

]