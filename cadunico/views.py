# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.gis.gdal import SpatialReference,CoordTransform
from django.contrib.gis import gdal
from geoliberty.models import Municipio
from django.template import RequestContext
from cadunico.models import MunicipioCadUnico, MunicipioBeneficiado

def Inicio(request):

    return render_to_response('inicio_cadunico.html', RequestContext(request,{}))

def MunicipiosCadUnico(request):
    
    obj = MunicipioCadUnico.objects.all()
    ct = CoordTransform(SpatialReference('EPSG:4326'), SpatialReference('EPSG:900913'))
    
    dados = []    
    for p in obj:
        p.municipio.mpoly.transform(ct)
    
    return render_to_response('mapa_cadunico.html', RequestContext(request,{'dados':dados,'municipios':obj}))

def CadastrosGerais(request):

    obj = MunicipioBeneficiado.objects.all().order_by('municipio__municipio')

    return render_to_response('cadastros_gerais.html', RequestContext(request,{'municipios':obj}))

def ExtratoRendaFamilias(request):

    obj = MunicipioBeneficiado.objects.all().order_by('municipio__municipio')

    return render_to_response('extratos_renda_familias.html', RequestContext(request,{'municipios':obj}))

def ExtratoRendaPessoas(request):

    obj = MunicipioBeneficiado.objects.all().order_by('municipio__municipio')

    return render_to_response('extratos_renda_pessoas.html', RequestContext(request,{'municipios':obj}))