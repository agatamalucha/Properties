from django.urls import path
from ballincollig.views import ballincollig_properties, search_property

app_name = "ballincollig"

urlpatterns = [

    path("", ballincollig_properties, name="ballincollig"),
    path("search_property", search_property, name="search_property" ),

]