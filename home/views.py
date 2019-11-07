from django.shortcuts import render
from .forms import *
from products.models import *
from repairs.models import *
from reviews.models import *

def home(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_phones = all_products.filter(product__category__id=1)
    products_laptops = all_products.filter(product__category__id=2)
    products_cables = all_products.filter(product__category__id=3)
    all_reviews = ReviewImage.objects.filter(is_active=True, is_main=True, review__is_active=True)

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

def iPhone_XS(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_iphone_XS = all_products.filter(product__category__id=13)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'iPhone_XS/iPhone_XS.html', locals())

def iPhone_XR(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_iphone_XR = all_products.filter(product__category__id=14)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'iPhone_XR/iPhone_XR.html', locals())

def iPhone_8(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_iphone_8 = all_products.filter(product__category__id=15)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'iPhone_8/iPhone_8.html', locals())

def iPhone_7(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_iphone_7 = all_products.filter(product__category__id=16)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'iPhone_7/iPhone_7.html', locals())

def apple_laptops(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_apple_laptops = all_products.filter(product__category__id=17)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'apple_laptops/apple_laptops.html', locals())

def iMac(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_iMac = all_products.filter(product__category__id=18)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'iMac/iMac.html', locals())

def watch(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'accessories/watch.html', locals())

def watch_series_5(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_watch_series_5 = all_products.filter(product__category__id=19)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'watch_series_5/watch_series_5.html', locals())

def watch_series_4(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_watch_series_4 = all_products.filter(product__category__id=20)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'watch_series_4/watch_series_4.html', locals())

def watch_series_3(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_watch_series_3 = all_products.filter(product__category__id=21)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'watch_series_3/watch_series_3.html', locals())

def watch_nike(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_watch_nike = all_products.filter(product__category__id=22)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'watch_nike/watch_nike.html', locals())

def iPades(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'iPades/iPades.html', locals())

def iPad(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_iPad = all_products.filter(product__category__id=23)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'iPad/iPad.html', locals())

def iPad_pro(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_iPad_pro = all_products.filter(product__category__id=24)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'iPad_pro/iPad_pro.html', locals())

def iPad_air(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_iPad_air = all_products.filter(product__category__id=25)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'iPad_air/iPad_air.html', locals())

def iPad_mini(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_iPad_mini = all_products.filter(product__category__id=26)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'iPad_mini/iPad_mini.html', locals())

def quadrocopter(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_quadrocopter = all_products.filter(product__category__id=27)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'quadrocopter/quadrocopter.html', locals())

def action_camera(request):

    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    new_products = all_products.filter(product__status__id=1)
    products_action_camera = all_products.filter(product__category__id=28)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'action_camera/action_camera.html', locals())

def repairs(request):

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["email"])
        new_form = form.save()

    return render(request, 'repairs/repairs.html', locals())
