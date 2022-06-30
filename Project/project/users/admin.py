from django.contrib import admin
from django.contrib.auth.models import User
from .models import profile
from properties.models import Property

admin.site.register(profile)
