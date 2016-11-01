from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from cadunico.views import MunicipiosCadUnico, Inicio, CadastrosGerais, ExtratoRendaFamilias, ExtratoRendaPessoas, GraficoMunicipio, BeneficiadosMunicipio

admin.autodiscover()

urlpatterns = patterns('cadunico',
                       
     url(r'^$',Inicio),
     url(r'^mapa/$',MunicipiosCadUnico),
     url(r'^cadastros-gerais/$',CadastrosGerais),
     url(r'^extrato-renda-familias/$',ExtratoRendaFamilias),
     url(r'^extrato-renda-pessoas/$',ExtratoRendaPessoas),
     url(r'^grafico-municipio/$',GraficoMunicipio),
     url(r'^beneficiados-municipio/$',BeneficiadosMunicipio),
)