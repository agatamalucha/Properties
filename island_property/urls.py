from django.urls import path
from . import views

app_name = "island_property"


urlpatterns = [
    path('', views.island_home, name='island-home'),
    path('search', views.island_search, name ='island-search'),

    ]

