import django_filters
from .models import Property
from django_filters import DateFilter
from django import forms


class PropertyFilter(django_filters.FilterSet):

    class Meta:
        model = Property
        fields = {'type': ['exact'],
                  'price': ['exact'], }
        #   'title': ['exact'], }}
