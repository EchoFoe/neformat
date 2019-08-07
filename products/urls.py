from django.conf.urls import url, include
from django.contrib import admin
from products import views
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^products/(?P<product_id>\w+)/$', views.product, name='product'),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)