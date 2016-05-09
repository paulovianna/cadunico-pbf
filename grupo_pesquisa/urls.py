from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from grupo_pesquisa.views import Inicio

admin.autodiscover()

urlpatterns = patterns('grupo_pesquisa',
                       
     url(r'^$',Inicio),
)