from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from datetime import datetime
import joblib


class HomeView(TemplateView):
    template_name = 'pages/index.html'


class AboutUs(TemplateView):
    template_name = 'aboutUs.html'


class Setting(TemplateView):
    template_name = 'settings.html'


def Prediction(request):
    cls = joblib.load('finalized_model (1).sav')
    print("hello1")
    lis = []
    lis.append(request.GET['bedrooms'])
    lis.append(request.GET['bathrooms'])
    lis.append(request.GET['SQFT_Living'])
    lis.append(request.GET['SQFT_lot'])
    lis.append(request.GET['floors'])
    lis.append(request.GET['waterfront'])
    lis.append(request.GET['condition'])
    lis.append(request.GET['grade'])
    lis.append(request.GET['SQFT_above'])
    lis.append(request.GET['SQFT_lot15'])
    lis.append(request.GET['yr_built'])
    lis.append(request.GET['SQFT_living15'])
    lis.append(request.GET['lat'])
    lis.append(request.GET['long'])
    print("hello2")

    ans = cls.predict([lis])
    return render(request, "result.html", {'ans': ans})
