from django.urls import path
from ballincollig.views import ballincollig_properties, search_property, search_area, ballincollig_year, search_year, search_year_query

app_name = "ballincollig"

urlpatterns = [

    path("", ballincollig_properties, name="ballincollig"),
    path("search-property", search_property, name="search-property"),
    path("search-area", search_area, name="search-area"),
    path("ballincollig-year", ballincollig_year, name="ballincollig-year"),
    path("search-year", search_year, name="search-year"),
    path("search-year-query", search_year_query, name="search-year-query"),


]
