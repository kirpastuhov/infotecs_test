from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class GetNumber(forms.Form):
    your_number = forms.IntegerField(label="Input number", max_value=10000, min_value=0)
