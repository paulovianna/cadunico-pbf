# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from workshop.views import Inicio

admin.autodiscover()

urlpatterns = patterns('workshop',
                       
     url(r'^$',Inicio),
)