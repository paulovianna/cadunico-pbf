# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.gis.gdal import SpatialReference,CoordTransform
from django.contrib.gis import gdal
from django.template import RequestContext
from cadunico.models import MunicipioCadUnico

def MunicipiosCadUnico(request):
    
    obj = MunicipioCadUnico.objects.all()
    ct = CoordTransform(SpatialReference('EPSG:4326'), SpatialReference('EPSG:900913'))
    
    dados = []    
    for p in obj:
        p.municipio.mpoly.transform(ct)
    
    return render_to_response('mapa_cadunico.html',
                              RequestContext(request,{'dados':dados,
                                                      'municipios':obj}))
