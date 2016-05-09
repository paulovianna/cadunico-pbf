from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from views import *
from grupo_pesquisa.views import Inicio as InicioGrupoPesquisa

admin.autodiscover()

urlpatterns = patterns('',
                       
     url(r'^admin/', include(admin.site.urls)),
     url(r'^upload/$',upload),
     url(r'^geoliberty/$',Inicio),
     url(r'^paises/$',Paises),
     url(r'^paises/pais/(?P<id_pais>\d+)/$',Mapa_Pais),
     url(r'^regioes/$',Regioes),
     url(r'^regioes/regiao/(?P<id_regiao>\d+)/$',Mapa_Regiao),
     url(r'^estados/$',Estados),
     url(r'^estados/estado/(?P<id_estado>\d+)/$',Mapa_Estado),
     url(r'^mesorregioes/$',Mesorregioes),
     url(r'^mesorregioes/mesorregiao/(?P<id_meso>\d+)/$',Mapa_Meso),
     url(r'^microrregioes/$',Microrregioes),
     url(r'^microrregioes/microrregiao/(?P<id_micro>\d+)/$',Mapa_Micro),
     url(r'^municipios/$',Municipios),
     url(r'^municipios/municipio/(?P<id_municipio>\d+)/$',Mapa_Municipio),
     url(r'^geopoliticas/$',RegioesGeopoliticas),
     url(r'^geopoliticas/geopolitica/(?P<id_geopolitica>\d+)/$',RegiaoGeopolitica),
     # Required to make static serving work 
     url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
     url(r'^amzop/', include('cadunico.urls')),
     url(r'^meso-mercosul/', include('cadunico_meso_mercosul.urls')),
     url(r'^$',InicioGrupoPesquisa),
)
