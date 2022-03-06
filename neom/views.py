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
    df = df.to_html(index=False)
    # print(r.json())
    # to pandas
    # display as basic pandas table
    return render(request, "jobs.html", { "df":df})

