from django import forms
from .models import *


class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        exclude = ['created', 'updated']