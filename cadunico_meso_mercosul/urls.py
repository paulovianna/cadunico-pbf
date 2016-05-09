from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from cadunico_meso_mercosul.views import Inicio

admin.autodiscover()

urlpatterns = patterns('meso-mercosul',
                       
     url(r'^$',Inicio),
)