from django import forms
from django.forms import ModelForm
from .models import Auto


class AutoForm(ModelForm):

    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'color', 'precio']