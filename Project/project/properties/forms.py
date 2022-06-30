
# forms.py
from django import forms
from .models import *

from django.contrib.auth import password_validation

from django import forms
import django
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import CharField
from django.utils.translation import gettext, gettext_lazy as _
# TYPE_CHOICES = (
#     ('1', 'rent'),
#     ('2', 'sell')
# )


class UploadForm(forms.ModelForm):

    city = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Coupon code',
        'aria-label': "Recipient's username",
        'aria-describedby': "basic-addon2",
    }))
    prop_kind = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Coupon code',
        'aria-label': "Recipient's username",
        'aria-describedby': "basic-addon2",
    }))

    # type = forms.ChoiceField(widget=forms.RadioSelect, choices=TYPE_CHOICES)
    videos = forms.CharField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        'placeholder': 'Coupon code',
        'aria-label': "Recipient's username",
        'aria-describedby': "basic-addon2",
    }))
    images = forms.CharField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        'placeholder': 'Coupon code',
        'aria-label': "Recipient's username",
        'aria-describedby': "basic-addon2",
    }))

    class Meta:
        model = UploadedProb
        fields = ['location', 'city', 'prop_kind', 'type', 'images', 'videos']


class Signupform (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
