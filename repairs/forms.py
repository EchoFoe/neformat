from django import forms
from .models import *


class StatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        exclude = ['created', 'updated']

class Form(forms.ModelForm):
    class Meta:
        model = Repair
        exclude = ['created', 'updated']