from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [

    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    # url(r'^cart/$', views.cart, name='cart'),
    url(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)