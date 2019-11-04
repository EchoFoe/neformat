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
    url(r'^iPhone_11/$', views.iPhone_11, name='iPhone_11'),
    url(r'^iPhone_11_pro/$', views.iPhone_11_pro, name='iPhone_11_pro'),
    url(r'^iPhone_XS/$', views.iPhone_XS, name='iPhone_XS'),
    url(r'^iPhone_XR/$', views.iPhone_XR, name='iPhone_XR'),
    url(r'^iPhone_8/$', views.iPhone_8, name='iPhone_8'),
    url(r'^iPhone_7/$', views.iPhone_7, name='iPhone_7'),
    url(r'^apple_laptops/$', views.apple_laptops, name='apple_laptops'),
    url(r'^iMac/$', views.iMac, name='iMac'),
    url(r'^watch/$', views.watch, name='watch'),
    url(r'^watch_series_5/$', views.watch_series_5, name='watch_series_5'),
    url(r'^watch_series_4/$', views.watch_series_4, name='watch_series_4'),
    url(r'^watch_series_3/$', views.watch_series_3, name='watch_series_3'),
    url(r'^watch_nike/$', views.watch_nike, name='watch_nike'),
    url(r'^iPades/$', views.iPades, name='iPades'),
    url(r'^iPad/$', views.iPad, name='iPad'),
    url(r'^iPad_pro/$', views.iPad_pro, name='iPad_pro'),
    url(r'^iPad_air/$', views.iPad_air, name='iPad_air'),
    url(r'^iPad_mini/$', views.iPad_mini, name='iPad_mini'),
    url(r'^quadrocopter/$', views.quadrocopter, name='quadrocopter'),
    url(r'^action_camera/$', views.action_camera, name='action_camera'),

]
