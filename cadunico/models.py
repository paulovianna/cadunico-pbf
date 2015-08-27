# -*- coding: utf-8 -*-
from django.db import models
from geoliberty.models import Municipio

class MunicipioCadUnico(models.Model):

    municipio = models.ForeignKey(Municipio, verbose_name='Município')
    populacao = models.FloatField('População')
    p_cadunico = models.FloatField('População CadUnico')
    f_cadunico = models.FloatField('Famílias CadUnico')
    f_atendidas_cadunico = models.FloatField('Famílias Atendidas CadUnico')

    class Meta:
        verbose_name = u'Municipios CadUnico'
        verbose_name_plural = u'Municipios CadUnico'

    def __unicode__(self):
        return self.municipio.municipio

    def porc_populacao_cadunico(self):
        return (int)((self.p_cadunico/self.populacao)*100)
    
    def porc_f_atendidas(self):
        return (int)((self.f_atendidas_cadunico/self.f_cadunico)*100)
