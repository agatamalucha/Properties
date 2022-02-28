from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.template.defaulttags import register
from core.models import BallincolligPropertyModel
from django.db.models import Sum
from django.http import HttpResponse

import pandas as pd
from django.shortcuts import render


@login_required
def neom_home(request):
    return render(request, "dashboard.html")
