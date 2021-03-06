from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [

    url(r'repairs/$', views.repairs, name='repairs'),
    url(r'^repairs/(?P<repair_id>\w+)/$', views.repair, name='repair'),

] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)