from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from core.models import BallincolligPropertyModel
from django.db.models import Sum
import pandas as pd


@login_required
def ballincollig_properties(request):
    properties = BallincolligPropertyModel.objects.all().values()
    dataset = pd.DataFrame(data=properties)
    dataset = dataset.drop("id",axis=1)
    dataset = dataset.to_html(index=False)
    return render(request, "ballincollig-properties.html",{"properties": properties, "dataset": dataset})
