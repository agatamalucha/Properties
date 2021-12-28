from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.template.defaulttags import register
from core.models import BallincolligPropertyModel
from django.db.models import Sum
import pandas as pd


@login_required
def ballincollig_properties(request):

    query = 'SELECT * FROM core_ballincolligpropertymodel'
    properties =  BallincolligPropertyModel.objects.raw(query)

    #properties = BallincolligPropertyModel.objects.all().values()
    # Raw SQL Query
    #dataset = pd.DataFrame(data=properties)
    dataset = pd.DataFrame([item.__dict__ for item in properties])
    dataset = dataset.drop(["id","_state"],axis=1)
    dataset = dataset.to_html(index=False)
    return render(request, "ballincollig-properties.html",{"properties": properties, "dataset": dataset})
