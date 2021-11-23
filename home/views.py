from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register
from django.db.models import Sum


@register.filter
def get_range(value):
    return range(value)

@login_required
def dashboard(request):
    return render(request, "dashboard.html", )

@login_required
def home(request):
    return render(request, "home.html", )