from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from core.models import BallincolligPropertyModel
from django.db.models import Sum
import pandas as pd


@register.filter
def get_range(value):
    return range(value)

@login_required
def dashboard(request):
    return render(request, "dashboard.html", )

@login_required
def home(request):
    properties = BallincolligPropertyModel.objects.all().values()
    dataset = pd.DataFrame(data=properties)
    dataset = dataset.to_html()
    return render(request, "home.html",{"properties": properties, "dataset": dataset})

@login_required
def ballincollig_properties(request):
    properties = BallincolligPropertyModel.objects.all()
    dataset = pd.DataFrame(data=properties)
    dataset = dataset.to_html()
    return render(request, "ballincollig-properties.html",{"properties": properties, "dataset": dataset})
