from django.urls import path
from . import views

app_name = "neom"

urlpatterns = [
    path('', views.neom_home, name='neom-home'),
    path('search', views.neom_search, name ='neom-search'),
]