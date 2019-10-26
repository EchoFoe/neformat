from django.shortcuts import render
from .forms import *
from products.models import *
from repairs.models import *

def home(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_phones = all_products.filter(product__category__id=1)
    products_laptops = all_products.filter(product__category__id=2)
    products_cables = all_products.filter(product__category__id=3)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'home/home.html', locals())

def smartphones(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_phones = all_products.filter(product__category__id=1)
    products_iphone_11 = all_products.filter(product__category__id=11)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'smartphones/smartphones.html', locals())

def laptops(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_laptops = all_products.filter(product__category__id=2)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'laptops/laptops.html', locals())

def cables(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_cables = all_products.filter(product__category__id=3)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'accessories/cables.html', locals())

def iphone_case(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_iphone_case = all_products.filter(product__category__id=4)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'accessories/iphone_case.html', locals())

def power_bank(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_power_bank = all_products.filter(product__category__id=5)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'accessories/power_bank.html', locals())

def audio_system(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_audio_system = all_products.filter(product__category__id=6)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'accessories/audio_system.html', locals())

def holder(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_holder = all_products.filter(product__category__id=7)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'accessories/holder.html', locals())

def glass_film(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_glass_film = all_products.filter(product__category__id=8)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'accessories/glass_film.html', locals())

def wall_charger(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_wall_charger = all_products.filter(product__category__id=9)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'accessories/wall_charger.html', locals())

def other(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_other = all_products.filter(product__category__id=10)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'accessories/other.html', locals())

def iPhone_11(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_iphone_11 = all_products.filter(product__category__id=11)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'iPhone_11/iPhone_11.html', locals())


def iPhone_11_pro(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_iphone_11_pro = all_products.filter(product__category__id=12)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'iPhone_11_pro/iPhone_11_pro.html', locals())

def repairs(request):

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'repairs/repairs.html', locals())
