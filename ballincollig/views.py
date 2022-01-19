from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.template.defaulttags import register
from core.models import BallincolligPropertyModel
from django.db.models import Sum
import pandas as pd


@login_required
def ballincollig_properties(request):
    areas = ['Maglin', 'Old Quarter', 'An Caislean','Muskerry Estate','Greenfield','Classis Lake',]
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
    areas = ['Maglin', 'Old Quarter', 'An Caislean', 'Muskerry Estate','Greenfield','Classis Lake', ]
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



@login_required
def search_area(request):
    areas = ['Maglin', 'Old Quarter', 'An Caislean', 'Muskerry Estate', 'Greenfield', 'Classis Lake', ]
    query = request.GET['sql_query']

    # SELECT * FROM core_ballincolligpropertymodel WHERE area = "Maglin"

    sql_query = f'{query}'
    sql_query= sql_query.replace( "properties","core_ballincolligpropertymodel")

    if "=" in sql_query and '"' not in sql_query and "AND" not in sql_query:
        param = sql_query.split("= ")[1].title()
        sql_query = sql_query.split("=")[0] + '= "' + param + '"'
        print(sql_query)

    properties = BallincolligPropertyModel.objects.raw(sql_query)

    if len(properties) > 0:
        # properties = BallincolligPropertyModel.objects.all().values()
        # Raw SQL Query
        # dataset = pd.DataFrame(data=properties)
        dataset = pd.DataFrame([item.__dict__ for item in properties])
        dataset = dataset.drop(["id", "_state"], axis=1)
        dataset = dataset.to_html(index=False)

    else:
        dataset = pd.DataFrame()

    return render(request, "ballincollig-properties.html", {"properties": properties, "dataset":dataset,"areas": areas, })


"""
SEARCH BY YEAR
"""



@login_required
def ballincollig_year(request):
    years = ['2021', '2020', '2019', '2018', ]
    query = 'SELECT * FROM core_ballincolligpropertymodel'
    properties =  BallincolligPropertyModel.objects.raw(query)
    #properties = BallincolligPropertyModel.objects.all().values()
    # Raw SQL Query
    #dataset = pd.DataFrame(data=properties)
    dataset = pd.DataFrame([item.__dict__ for item in properties])
    dataset = dataset.drop(["id", "_state"], axis=1)
    dataset = dataset.to_html(index=False)
    return render(request, "ballincollig-properties-year.html",{"properties": properties, "dataset": dataset,"years": years })



@login_required
def search_year(request):
    years = ['2021', '2020', '2019', '2018', ]
    year = request.GET['year']
    query = f'SELECT * FROM core_ballincolligpropertymodel WHERE sold_date LIKE "{year}%" '
    properties =  BallincolligPropertyModel.objects.raw(query)
    #properties = BallincolligPropertyModel.objects.all().values()
    # Raw SQL Query
    #dataset = pd.DataFrame(data=properties)
    dataset = pd.DataFrame([item.__dict__ for item in properties])
    dataset = dataset.drop(["id", "_state"], axis=1)
    dataset = dataset.to_html(index=False)
    return render(request, "ballincollig-properties-year.html",{"properties": properties, "dataset": dataset,"years": years })


@login_required
def search_year_query(request):

    years = ['2021', '2020', '2019', '2018', ]
    query = request.GET['sql_query']

    # SELECT * FROM core_ballincolligpropertymodel LIKE sold_date = "2020"

    sql_query = f'{query}'
    sql_query= sql_query.replace( "properties","core_ballincolligpropertymodel")

    if "LIKE" in sql_query and '"' not in sql_query and "AND" not in sql_query:
        param = sql_query.split("LIKE ")[1].title()
        sql_query = sql_query.split("LIKE")[0] + 'LIKE "' + param + '"'
        print(sql_query)

    properties = BallincolligPropertyModel.objects.raw(sql_query)

    if len(properties) > 0:
        # properties = BallincolligPropertyModel.objects.all().values()
        # Raw SQL Query
        # dataset = pd.DataFrame(data=properties)
        dataset = pd.DataFrame([item.__dict__ for item in properties])
        dataset = dataset.drop(["id", "_state"], axis=1)
        dataset = dataset.to_html(index=False)

    else:
        dataset = pd.DataFrame()

    return render(request, "ballincollig-properties-year.html", {"properties": properties, "dataset":dataset,"years": years, })

