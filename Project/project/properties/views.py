
from .models import Property
from .models import PropImage
from .models import UploadedProb
from .filters import PropertyFilter

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpRequest

from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages


from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, Paginator

import joblib
import xgboost as xgb
# def property(request):
#     the_Property = Property.objects.all()1

#     return render(request, 'pages/index.html', {'house': the_Property})

# product.objects.get(name=habiba)
# def detail(request):
#     Notes = Property.objects.all()
#     return render(request, 'pages/details_page.html', {'note': Notes})


class Details(TemplateView):
    template_name = 'details_page.html'


class HouseView(ListView):

    template_name = 'house.html'
    model = Property
    context_object_name = "houses"


class HouseDetails(DetailView):
    model = Property
    context_object_name = "house"
    template_name = 'details_page.html'


class Sell12(TemplateView):
    template_name = 'sell1,2.html'


# class Sell3(TemplateView):
#     template_name = 'sell 3.html'


class Sell4(TemplateView):
    template_name = 'sell-4.html'


class Filter(TemplateView):
    template_name = 'onboaded i.html'


class Filter2(TemplateView):
    template_name = 'onboaded ii.html'


class Filter3(TemplateView):
    template_name = 'onboaded iii.html'


class ThankYou(TemplateView):
    template_name = 'thank_you.html'


class Result(TemplateView):
    template_name = 'result.html'


class index(TemplateView):
    template_name = 'pages/index.html'


# def upload(request):
#     if request.method == 'POST':
#         images = ['']

#         new = UploadedProb.objects.create_new(images=images)

#     else:
#         return(request, 'pages/index.html')


def PropView(request):  # AllHousesView

    properties = Property.objects.all()
    myFilter = PropertyFilter(request.GET, queryset=properties)
    properties = myFilter.qs
    properties_paginator = Paginator(properties, 5)
    page_num = request.GET.get('page')

    page = properties_paginator.get_page(page_num)
    context = {
        'page': page,
        'count': properties_paginator.count,
        'myFilter': myFilter,

    }
    return render(request, 'all_properties.html', context)


def detail_view(request, id):  # detailhouseview
    property = get_object_or_404(Property, id=id)
    photos = PropImage.objects.filter(property=property)
    return render(request, 'details_page.html', {
        'property': property,
        'photos': photos
    })
    # def house(request):
    #     return render(request, 'pages/index.html', {'x': Property.objects.filter(price=)})


# def showthis(request):
#     Property.objects.all().delete
#     # deletes all objects from Car database table

#     context = {}
#     return render(request, 'pages/index.html', context)
# def uploadProperty(request):

# this function take the inputs  from the form in inboadedIII and deploy the ML model
def Prediction(request):
    print("hello0")

    # booster = xgboost.Booster()
    # booster.load_model('model_file_name.json')
    model2 = xgb.XGBRegressor()
    model2.load_model("final_model.bin")
    # cls = joblib.load('model.json')
    print("hello1")
    print(request.GET)
    lis = []
    # list = [2, 1, 1220, 6300, 1.0, 0, 3, 7, 760,
    #         1942, 47.5299, -122.387, 1850, 4886]
    lis.append(int(request.GET['bedrooms']))
    print(request.GET['bedrooms'])
    lis.append(float(request.GET['bathrooms']))
    print(request.GET['bathrooms'])

    lis.append(int(request.GET['SQFT_Living']))
    print(request.GET['SQFT_Living'])
    lis.append(int(request.GET['SQFT_lot']))
    print(request.GET['SQFT_lot'])
    lis.append(float(request.GET['floors']))
    print(request.GET['floors'])
    lis.append(int(request.GET['waterfront']))
    print(request.GET['waterfront'])
    lis.append(int(request.GET['condition']))
    print(request.GET['condition'])
    lis.append(int(request.GET['grade']))
    print(request.GET['grade'])
    lis.append(int(request.GET['SQFT_above']))
    print(request.GET['SQFT_above'])
    lis.append(int(request.GET['yr_built']))
    print(request.GET['yr_built'])
    lis.append(float(request.GET['lat']))
    print(request.GET['lat'])
    lis.append(float(request.GET['long']))
    print(request.GET['long'])

    lis.append(int(request.GET['SQFT_living15']))
    print(request.GET['SQFT_living15'])
    lis.append(int(request.GET['SQFT_lot15']))
    print(request.GET['SQFT_lot15'])

    print("hello2")

    ans = model2.predict([lis])
    return render(request, "result.html", {'ans': ans})


def sell3(request):
    # print("hello1")
    # if request.method == "POST":
    #     print("hello0")
    #     type = request.POST['type']
    #     location = request.POST['location']
    #     # city = request.POST['city']
    #     prop_type = request.POST['prop_type']
    #     images = request.FILES['images']
    #     videos = request.FILES['videos']

    #     myprop = UploadedProb.objects.create_upload(type,
    #                                                 location,  prop_type)
    #     myprop.images = images
    #     myprop.videos = videos
    #     print("hello2")

    #     # myuser.is_active = False
    #     myprop.is_active = False
    #     myprop.save()
    #     print("hello3")
    # return render(request, "sell 3.html")

    if request.method == 'POST':

        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            print("sav")
            return redirect('sell4')
    else:
        form = UploadForm()

    return render(request, 'sell 3.html', {'form': form})
