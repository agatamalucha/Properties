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
def island_home(request):
    r = requests.get('http://data-collector.mycaprover.toutf.com/island-properties/properties/')
    txt = r.json()
    data = txt['results']
    df = pd.DataFrame(data)
    unique_localities =list(df["locality"].unique())
    advert_type_df = df[df["advert_type"] == "sale"]
    advert_type_df["price_per_sq_meter"] = advert_type_df["price"]/advert_type_df["size"]
    island_average_sale =advert_type_df.groupby(["island"])["price_per_sq_meter"].mean()
    gran_canaria = island_average_sale[0]
    lanzerote = island_average_sale[1]
    mallorca = island_average_sale[2]
    tenerife = island_average_sale[3]

    if request.method == "POST":
        div = request.POST["unique_locality"]
        df = df[df["locality"] == div]
        df = df.to_html(index=False)
        return render(request, "island.html", {"df": df, "unique_localities":unique_localities})

    df = df.to_html(index=False)
    return render(request, "island.html", {"df": df, "unique_localities":unique_localities,
                                           "island_average_sale":island_average_sale,
                                           "gran_canaria":gran_canaria,
                                           "lanzerote":lanzerote,
                                           "mallorca":mallorca,
                                           "tenerife":tenerife,

                                           })


@login_required
def island_search(request):
    r = requests.get('http://data-collector.mycaprover.toutf.com/island-properties/properties/')
    txt = r.json()
    data = txt['results']
    df = pd.DataFrame(data)

    if request.method == "POST":
        div = request.POST["search_words"]
        df = df[df['island'].str.contains(div)]
        #print(div)
        df = df.to_html(index=False)
        return render(request, "island.html", {"df": df })
    df = df.to_html(index=False)
    return render(request, "island.html", { "df":df })

