from django.shortcuts import render
from .forms import *

def contacts(request):

    form = SupportForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data['name'])
        new_form = form.save()

    return render(request, 'contacts/contacts.html', locals())