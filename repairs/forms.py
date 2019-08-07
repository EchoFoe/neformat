from django import forms
from .models import *


class StatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        exclude = ['created', 'updated']