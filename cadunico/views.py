# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.gis.gdal import SpatialReference,CoordTransform
from django.contrib.gis import gdal
from geoliberty.models import Municipio
from django.template import RequestContext
from cadunico.models import MunicipioCadUnico, MunicipioBeneficiado, EstadoBeneficiado, PaisBeneficiado

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

    mun = MunicipioBeneficiado.objects.filter(pessoas_cadunico_d__year='2016', pessoas_cadunico_d__month='05', pessoas_cadunico_d__day='05').order_by('municipio__municipio')
    est = EstadoBeneficiado.objects.all().order_by('estado__uf')
    pais = PaisBeneficiado.objects.all().order_by('pais__pais')
    total = 0
    for o in mun:
        total = total + o.valor_pago
    return render_to_response('cadastros_gerais.html', RequestContext(request,{'municipios':mun,'estados':est,'total':total,'pais':pais}))

def ExtratoRendaFamilias(request):

    obj = MunicipioBeneficiado.objects.filter(pessoas_cadunico_d__year='2016', pessoas_cadunico_d__month='05', pessoas_cadunico_d__day='05').order_by('municipio__municipio')
    est = EstadoBeneficiado.objects.all().order_by('estado__uf')
    pais = PaisBeneficiado.objects.all().order_by('pais__pais')

    return render_to_response('extratos_renda_familias.html', RequestContext(request,{'municipios':obj,'estados':est,'pais':pais}))

def ExtratoRendaPessoas(request):

    obj = MunicipioBeneficiado.objects.filter(pessoas_cadunico_d__year='2016', pessoas_cadunico_d__month='05', pessoas_cadunico_d__day='05').order_by('municipio__municipio')
    est = EstadoBeneficiado.objects.all().order_by('estado__uf')
    pais = PaisBeneficiado.objects.all().order_by('pais__pais')

    return render_to_response('extratos_renda_pessoas.html', RequestContext(request,{'municipios':obj,'estados':est,'pais':pais}))

def GraficoMunicipio(request):

    municipios = MunicipioBeneficiado.objects.all().order_by('municipio__municipio').distinct('municipio__municipio')

    return render_to_response('grafico_municipio_cadunico.html', RequestContext(request,{'municipios':municipios, 'nome':'Selecione um Município'}))

def BeneficiadosMunicipio(request):

    id = request.POST.get('municipio')
    print request.POST.get('municipio')
    nome = ''
    municipios = MunicipioBeneficiado.objects.all().order_by('municipio__municipio').distinct('municipio__municipio')
    dados = MunicipioBeneficiado.objects.filter(municipio__id=id)
    for d in dados:
        nome = d.municipio.municipio

    return render_to_response('grafico_municipio_cadunico.html', RequestContext(request,{'municipios':municipios, 'dados':dados, 'nome':nome}))