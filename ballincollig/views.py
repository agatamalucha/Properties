from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.template.defaulttags import register
from core.models import BallincolligPropertyModel
from django.db.models import Sum
import pandas as pd


@login_required
def ballincollig_properties(request):
    areas = ['Maglin', 'Old Quarter', 'An Caislean','Muskerry Estate','Greenfield',]
    query = 'SELECT * FROM core_ballincolligpropertymodel'
    properties =  BallincolligPropertyModel.objects.raw(query)



    if len(properties) > 0:
        # properties = BallincolligPropertyModel.objects.all().values()
        # Raw SQL Query
        # dataset = pd.DataFrame(data=properties)
        dataset = pd.DataFrame([item.__dict__ for item in properties])
        dataset = dataset.drop(["id", "_state"], axis=1)
        dataset = dataset.to_html(index=False)

    else:
        dataset = pd.DataFrame()

    return render(request, "ballincollig-properties.html",{"properties": properties, "dataset": dataset, "areas": areas})



@login_required
def search_property(request):
    areas = ['Maglin', 'Old Quarter', 'An Caislean', 'Muskerry Estate','Greenfield', ]
    area = request.GET['area']
    query = f'SELECT * FROM core_ballincolligpropertymodel WHERE area = "{area}" '
    properties =  BallincolligPropertyModel.objects.raw(query)
    #properties = BallincolligPropertyModel.objects.all().values()
    # Raw SQL Query
    #dataset = pd.DataFrame(data=properties)
    dataset = pd.DataFrame([item.__dict__ for item in properties])
    dataset = dataset.drop(["id", "_state"], axis=1)
    dataset = dataset.to_html(index=False)
    return render(request, "ballincollig-properties.html",{"properties": properties, "dataset": dataset,"areas": areas })
