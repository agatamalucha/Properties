from django.urls import path
from home.views import home, dashboard, ballincollig_properties

app_name = "home"

urlpatterns = [

    path("",home, name="home"),
    path("dashboard",dashboard, name="dashboard"),
]