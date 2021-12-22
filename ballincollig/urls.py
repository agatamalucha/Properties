from django.urls import path
from ballincollig.views import ballincollig_properties

app_name = "ballincollig"

urlpatterns = [

    path("", ballincollig_properties, name="ballincollig"),

]