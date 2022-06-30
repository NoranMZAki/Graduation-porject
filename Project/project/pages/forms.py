from django import forms


class Loginform(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
