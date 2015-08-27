from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from cadunico.views import MunicipiosCadUnico

admin.autodiscover()

urlpatterns = patterns('cadunico',
                       
     url(r'^$',MunicipiosCadUnico),
)