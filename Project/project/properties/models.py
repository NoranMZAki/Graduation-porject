
from decimal import Decimal
from multiprocessing.sharedctypes import Value
from django.db import models
from datetime import datetime  # create intial datetime value
from django.contrib.auth.models import User
from xml.dom.minidom import CharacterData
from django.forms import CharField
from matplotlib.style import context
from users.models import profile
from datetime import datetime
from django.shortcuts import render


class property_type(models.Model):
    type = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.type


class Property(models.Model):

    bedrooms = models.IntegerField(
        null=True)
    bathrooms = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=0)
    SQFT_Living = models.IntegerField(
        null=True)
    SQFT_lot = models.IntegerField(
        null=True)
    floors = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=0)
    waterfront = models.IntegerField(
        null=True)
    view = models.IntegerField(
        null=True)
    condition = models.IntegerField(
        null=True)
    grade = models.IntegerField(
        null=True)
    SQFT_above = models.IntegerField(
        null=True)
    SQFT_basement = models.IntegerField(
        null=True)
    yr_built = models.IntegerField(
        null=True)
    yr_renovated = models.IntegerField(
        null=True)
    zip_code = models.IntegerField(
        null=True)
    lat = models.DecimalField(
        max_digits=7, decimal_places=4, null=True)

    long = models.DecimalField(
        max_digits=7, decimal_places=3, null=True, blank=0)

    SQFT_living15 = models.IntegerField(
        null=True)

    SQFT_lot15 = models.IntegerField(
        null=True)

    price = models.DecimalField(
        max_digits=10, decimal_places=3, null=True)

    created = models.DateTimeField(default=datetime.now)
    # user upload prop relation
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    city = models.CharField(max_length=50, null=True)
    type = models.ForeignKey(
        property_type, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)  # 0
    image = models.FileField(blank=True, null=True)
    active = models.BooleanField(default=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title  # return the house name in the admin panel


class PropImage(models.Model):
    property = models.ForeignKey(
        Property, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')


class UploadedProb(models.Model):  # model for user to upload properites
    type = models.ForeignKey(
        property_type, on_delete=models.CASCADE, null=True)
    prop_kind = models.CharField(max_length=100, null=True)
    images = models.ImageField(upload_to='images/', null=True)
    videos = models.FileField(upload_to='images/', null=True)
    city = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=300, null=True)
    location = models.URLField(null=True)
    profile = models.OneToOneField(

        profile, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.prop_kind
