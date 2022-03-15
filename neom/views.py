from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.template.defaulttags import register
from core.models import BallincolligPropertyModel
from django.db.models import Sum
from django.http import HttpResponse
import pandas as pd
from django.shortcuts import render
import requests
import json


@login_required
def neom_home(request):
    r = requests.get('https://data-collector.mycaprover.toutf.com/neom/jobs/')
    txt = r.json()
    data = txt['results']
    df = pd.DataFrame(data)
    unique_divisions = list(df['division'].unique())
    # to pandas
    # display as basic pandas table
    if request.method == "POST":
        div = request.POST["unique_division"]
        df = df[df["division"] == div]
        df = df.to_html(index=False)
        return render(request, "jobs.html", {"df": df, "unique_divisions": unique_divisions})
    df = df.to_html(index=False)
    return render(request, "jobs.html", { "df":df , "unique_divisions":unique_divisions})

@login_required
def neom_search(request):
    r = requests.get('https://data-collector.mycaprover.toutf.com/neom/jobs/')
    txt = r.json()
    data = txt['results']
    df = pd.DataFrame(data)

    if request.method == "POST":
        div = request.POST["search_words"]
        df = df[df['title'].str.contains(div)]
        #print(div)
        df = df.to_html(index=False)
        return render(request, "jobs.html", {"df": df })
    df = df.to_html(index=False)
    return render(request, "jobs.html", { "df":df  })
