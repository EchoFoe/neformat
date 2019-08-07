from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^smartphones/$', views.smartphones, name='smartphones'),
    url(r'^laptops/$', views.laptops, name='laptops'),
    url(r'cables/$', views.cables, name='cables'),
    url(r'iphone_case/$', views.iphone_case, name='iphone_case'),
    url(r'power_bank/$', views.power_bank, name='power_bank'),
    url(r'audio_system/$', views.audio_system, name='audio_system'),
    url(r'holder/$', views.holder, name='holder'),
    url(r'glass_film/$', views.glass_film, name='glass_film'),
    url(r'wall_charger/$', views.wall_charger, name='wall_charger'),
    url(r'other/$', views.other, name='other'),

]
