from django.shortcuts import render
from .forms import *
from repairs.models import *

def repairs(request):

    all_repairs = Repair.objects.filter(is_active=True)
    all_categories = RepairCategory.objects.filter(is_active=True)
    all_repairs2 = RepairImage.objects.filter(is_active=True, is_main=True, repair__is_active=True)

    form = StatementForm(request.POST or None)
    a = Form(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data['name'])
        new_form = form.save()
        new_a = a.save()

    return render(request, 'repairs/repairs.html', locals())

def repair(request, repair_id):
    repairs_link = Repair.objects.get(id=repair_id)
    all_repairs = Repair.objects.filter(is_active=True)
    all_categories = RepairCategory.objects.filter(is_active=True)
    all_repairs2 = RepairImage.objects.filter(is_active=True, is_main=True, repair__is_active=True)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'repairs/repair.html', locals())