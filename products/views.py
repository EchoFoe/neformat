from django.shortcuts import render
from products.models import *
from .forms import *
# from utils.uploadings import UploadingProducts
# from django.contrib import messages

def product(request, product_id):
    products = Product.objects.get(id=product_id)
    all_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    top_products = all_products.filter(product__top_sales=True)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'products/product.html', locals())